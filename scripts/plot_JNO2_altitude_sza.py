"""
Compute and plot J(NO2) = J(NO2 + hv -> NO + O(3P)) as a function of
altitude and solar zenith angle (SZA), using real tabulated data:

    sigma_O2(lambda)   data/O2_merged_50-250nm.csv          (MPI-Mainz)
    sigma_O3(lambda)   data/O3_merged_100-1000nm.csv         (MPI-Mainz)
    sigma_NO2(lambda)  data/NO2_merged_240-662.5nm.csv       (JPL-2010)
    phi_NO2(lambda)    data/NO2_QY_NO_O3P_298K.csv           (Troe 2000)
    F_TOA(lambda)      data/photon_flux_toa_surface_280-500nm.csv
    M(z)               data/us_standard_atmosphere_1976.csv  (1976 US Std Atm)

Method
------
1. Beer-Lambert attenuation of the TOA photon flux down to altitude z,
   using O2 + O3 as the two significant stratospheric/tropospheric
   absorbers (per the course notes, Sec. 3.1-3.2) -- NO2 itself absorbs
   too weakly and is present in too small a column to matter for its
   own attenuation.
2. The slant path length scales as sec(theta) for zenith angle theta
   (flat-atmosphere approximation -- breaks down close to the horizon,
   theta -> 90 deg, where sec(theta) diverges).
3. J(NO2)(z,theta) = integral over lambda of
       sigma_NO2(lambda) * phi_NO2(lambda) * F(lambda, z, theta) dlambda

Data coverage / assumptions (documented explicitly since this feeds a
lecture figure):

* O2 and O3 columns above z: the repo has no *measured* vertical profile
  for O3, so (as in the Module 3 notebook, Exercise 3) we use illustrative
  profiles: O2 well-mixed at 20.946% of the REAL US Standard Atmosphere
  number density M(z), and O3 as a Gaussian layer peaked at 25 km. This
  is the one part of the calculation that is still a toy -- everything
  else (cross sections, quantum yield, TOA flux) is real data.
* The NO2 quantum yield is tabulated over 300-415 nm only (Troe, 2000,
  298 K). Outside that range we hold it flat at the nearest tabulated
  value: phi=1.0 below 300 nm (matches the tabulated value at 300 nm,
  and NO2 photodissociation is known to have unit yield throughout the
  UV) and phi=0.06 (the 415 nm value) above 415 nm. The integration
  wavelength grid only extends to 500 nm anyway (limited by the TOA
  flux data), well past where phi has fallen close to zero.
* sec(theta) is capped at theta = 89 deg to avoid the sec(theta) -> inf
  singularity exactly at the horizon.

Requires: numpy, pandas, matplotlib
    pip install numpy pandas matplotlib

Run:
    python plot_JNO2_altitude_sza.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

# ---------------------------------------------------------------------------
# Wavelength grid: bounded by the TOA flux data (280-500 nm). This comfortably
# covers the NO2 photolysis window (~300-424 nm) and where it doesn't overlap
# with the tabulated NO2 quantum yield (300-415 nm) we extrapolate flat.
# ---------------------------------------------------------------------------
WL_MIN, WL_MAX, WL_STEP = 280.0, 500.0, 0.5  # nm
wl_grid = np.arange(WL_MIN, WL_MAX + WL_STEP, WL_STEP)

ALTITUDES_KM = np.linspace(0, 50, 51)          # 0-50 km, 1 km steps
SZA_CURVES_DEG = [0, 30, 60, 80]               # for the J vs altitude plot
ALT_CURVES_KM = [0, 15, 30, 45]                # for the J vs SZA plot
SZA_GRID_DEG = np.linspace(0, 89, 90)          # for the J vs SZA plot

O2_MIXING_RATIO = 0.20946


def load_xy(filename, xcol="wavelength_nm", ycol=None):
    df = pd.read_csv(DATA_DIR / filename)
    ycol = ycol or df.columns[1]
    df = df.sort_values(xcol)
    return df[xcol].to_numpy(), df[ycol].to_numpy()


def main():
    # --- Cross sections and quantum yield, interpolated onto wl_grid -------
    wl_o2, xs_o2 = load_xy("O2_merged_50-250nm.csv", ycol="cross_section_cm2")
    wl_o3, xs_o3 = load_xy("O3_merged_100-1000nm.csv", ycol="cross_section_cm2")
    wl_no2, xs_no2 = load_xy("NO2_merged_240-662.5nm.csv", ycol="cross_section_cm2")
    wl_qy, qy_no2 = load_xy("NO2_QY_NO_O3P_298K.csv", ycol="quantum_yield")

    # O2 has essentially zero absorption above ~245 nm (Herzberg continuum) --
    # outside its tabulated range, treat as zero rather than extrapolating.
    sigma_O2 = np.interp(wl_grid, wl_o2, xs_o2, left=0.0, right=0.0)
    sigma_O3 = np.interp(wl_grid, wl_o3, xs_o3, left=0.0, right=0.0)
    sigma_NO2 = np.interp(wl_grid, wl_no2, xs_no2, left=0.0, right=0.0)
    # NO2 quantum yield: hold flat at the edge values outside 300-415 nm
    # (see module docstring for the reasoning).
    phi_NO2 = np.interp(wl_grid, wl_qy, qy_no2, left=qy_no2[0], right=qy_no2[-1])

    # --- TOA photon flux, interpolated onto wl_grid ------------------------
    flux = pd.read_csv(DATA_DIR / "photon_flux_toa_surface_280-500nm.csv")
    F_TOA = np.interp(wl_grid, flux.wavelength_nm.to_numpy(),
                       flux.toa_photon_flux_per_s_cm2_nm.to_numpy())

    # --- Atmosphere: real M(z) from the US Standard Atmosphere, toy O3 -----
    atm = pd.read_csv(DATA_DIR / "us_standard_atmosphere_1976.csv")
    z_atm_km = atm.altitude_km.to_numpy()
    M_atm = atm.number_density_cm3.to_numpy()

    def M_total(z_km):
        return np.interp(z_km, z_atm_km, M_atm, right=0.0)

    def n_O2(z_km):
        return O2_MIXING_RATIO * M_total(z_km)

    def n_O3(z_km, peak=5e12, z_peak_km=25.0, width_km=7.0):
        # Illustrative Gaussian ozone layer (no measured profile in the repo)
        return peak * np.exp(-0.5 * ((z_km - z_peak_km) / width_km) ** 2)

    def column_above(z_km, n_func, z_top_km=86.0, n_steps=400):
        """Overhead column (molecules/cm^2) from z_km up to z_top_km."""
        zs_km = np.linspace(z_km, z_top_km, n_steps)
        return np.trapezoid(n_func(zs_km), zs_km * 1e5)  # km -> cm for the integral

    # Precompute O2/O3 columns at every altitude on our grid.
    col_O2_z = np.array([column_above(z, n_O2) for z in ALTITUDES_KM])
    col_O3_z = np.array([column_above(z, n_O3) for z in ALTITUDES_KM])

    def J_NO2(col_O2, col_O3, sza_deg):
        """J(NO2) (s^-1) at a single altitude (given its overhead O2/O3
        columns) and solar zenith angle."""
        airmass = 1.0 / np.cos(np.radians(min(sza_deg, 89.0)))
        OD_vertical = sigma_O2 * col_O2 + sigma_O3 * col_O3
        F_z = F_TOA * np.exp(-OD_vertical * airmass)
        integrand = sigma_NO2 * phi_NO2 * F_z
        return np.trapezoid(integrand, wl_grid)

    # --- Sanity check: clear-sky, overhead-sun surface J(NO2) --------------
    j_surface_overhead = J_NO2(col_O2_z[0], col_O3_z[0], 0.0)
    print(f"J(NO2) at z=0 km, SZA=0 deg: {j_surface_overhead:.3e} s^-1 "
          f"(literature clear-sky value ~ 8e-3 s^-1)")

    apply_style()

    # =========================================================================
    # Figure 1: J(NO2) vs altitude, one curve per SZA
    # =========================================================================
    fig1, ax1 = plt.subplots(figsize=FIGSIZE)
    for i, sza in enumerate(SZA_CURVES_DEG):
        J_vals = np.array([J_NO2(col_O2_z[k], col_O3_z[k], sza)
                            for k in range(len(ALTITUDES_KM))])
        ax1.plot(J_vals * 1e3, ALTITUDES_KM, color=COLORS[i % len(COLORS)],
                  lw=LINEWIDTH, label=f"SZA = {sza}$^\\circ$")

    ax1.set_xlabel("J(NO$_2$) (10$^{-3}$ s$^{-1}$)", fontsize=FONTSIZE)
    ax1.set_ylabel("Altitude (km)", fontsize=FONTSIZE)
    ax1.set_title("J(NO$_2$) vs altitude", fontsize=TITLE_FONTSIZE)
    ax1.tick_params(labelsize=FONTSIZE - 1)
    ax1.set_ylim(0, 50)
    ax1.set_xlim(left=0)
    ax1.legend(fontsize=FONTSIZE - 3, loc="upper left")
    fig1.tight_layout()
    fig1.savefig(FIGURES_DIR / "JNO2_vs_altitude.png", dpi=150)
    print("Saved JNO2_vs_altitude.png")

    # =========================================================================
    # Figure 2: J(NO2) vs solar zenith angle, one curve per altitude
    # =========================================================================
    fig2, ax2 = plt.subplots(figsize=FIGSIZE)
    for i, z in enumerate(ALT_CURVES_KM):
        col_O2_i = column_above(z, n_O2)
        col_O3_i = column_above(z, n_O3)
        J_vals = np.array([J_NO2(col_O2_i, col_O3_i, sza) for sza in SZA_GRID_DEG])
        ax2.plot(SZA_GRID_DEG, J_vals * 1e3, color=COLORS[i % len(COLORS)],
                  lw=LINEWIDTH, label=f"z = {z} km")

    ax2.set_xlabel("Solar zenith angle (degrees)", fontsize=FONTSIZE)
    ax2.set_ylabel("J(NO$_2$) (10$^{-3}$ s$^{-1}$)", fontsize=FONTSIZE)
    ax2.set_title("J(NO$_2$) vs solar zenith angle", fontsize=TITLE_FONTSIZE)
    ax2.tick_params(labelsize=FONTSIZE - 1)
    ax2.set_xlim(0, 89)
    ax2.set_ylim(bottom=0)
    ax2.legend(fontsize=FONTSIZE - 3, loc="lower left")
    fig2.tight_layout()
    fig2.savefig(FIGURES_DIR / "JNO2_vs_sza.png", dpi=150)
    print("Saved JNO2_vs_sza.png")

    # =========================================================================
    # Figure 3: 2D heatmap, J(NO2) as a function of both altitude and SZA
    # =========================================================================
    J_grid = np.zeros((len(ALTITUDES_KM), len(SZA_GRID_DEG)))
    for k in range(len(ALTITUDES_KM)):
        for j, sza in enumerate(SZA_GRID_DEG):
            J_grid[k, j] = J_NO2(col_O2_z[k], col_O3_z[k], sza)

    fig3, ax3 = plt.subplots(figsize=FIGSIZE)
    pcm = ax3.pcolormesh(SZA_GRID_DEG, ALTITUDES_KM, J_grid * 1e3,
                          shading="auto", cmap="inferno")
    cbar = fig3.colorbar(pcm, ax=ax3)
    cbar.set_label("J(NO$_2$) (10$^{-3}$ s$^{-1}$)", fontsize=FONTSIZE - 1)
    ax3.set_xlabel("Solar zenith angle (degrees)", fontsize=FONTSIZE)
    ax3.set_ylabel("Altitude (km)", fontsize=FONTSIZE)
    ax3.set_title("J(NO$_2$) vs altitude and SZA", fontsize=TITLE_FONTSIZE)
    ax3.tick_params(labelsize=FONTSIZE - 1)
    fig3.tight_layout()
    fig3.savefig(FIGURES_DIR / "JNO2_altitude_sza_heatmap.png", dpi=150)
    print("Saved JNO2_altitude_sza_heatmap.png")

    plt.show()


if __name__ == "__main__":
    main()
