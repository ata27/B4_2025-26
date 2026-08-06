"""
Plot the solar photon flux at the top of the atmosphere (AM0) and at
Earth's surface (AM1.5 global), converted from the ASTM G173 spectral
irradiance data, over 280-500 nm.

The ASTM G173 reference file only covers wavelengths >= 280 nm, so the
plot is restricted to 280-500 nm rather than the full 150-500 nm UV/VIS
range.

Data: data/astmg173.csv (ASTM G173-03 reference spectra)

Requires: pandas, matplotlib
    pip install pandas matplotlib

Run:
    python plot_photon_flux_toa_surface.py
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style, add_energy_axis

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

WL_MIN, WL_MAX = 280.0, 500.0  # nm - limited by ASTM G173 data coverage

# Planck constant, speed of light (SI) - to convert irradiance to photon flux
_PLANCK = 6.62607015e-34  # J s
_LIGHTSPEED = 2.99792458e8  # m/s


def irradiance_to_photon_flux(wavelength_nm, irradiance_W_m2_nm):
    """Convert spectral irradiance (W/m^2/nm) to photon flux (photons/s/cm^2/nm)."""
    wl_m = wavelength_nm * 1e-9
    photon_energy = _PLANCK * _LIGHTSPEED / wl_m
    flux_per_m2 = irradiance_W_m2_nm / photon_energy
    return flux_per_m2 * 1e-4  # m^-2 -> cm^-2


def main():
    df = pd.read_csv(DATA_DIR / "astmg173.csv")
    df.columns = ["wavelength_nm", "extraterrestrial", "global_tilt", "direct_circumsolar"]
    df = df[(df.wavelength_nm >= WL_MIN) & (df.wavelength_nm <= WL_MAX)]

    toa_flux = irradiance_to_photon_flux(df.wavelength_nm.to_numpy(), df.extraterrestrial.to_numpy())
    surface_flux = irradiance_to_photon_flux(df.wavelength_nm.to_numpy(), df.global_tilt.to_numpy())

    out = pd.DataFrame({
        "wavelength_nm": df.wavelength_nm,
        "toa_photon_flux_per_s_cm2_nm": toa_flux,
        "surface_photon_flux_per_s_cm2_nm": surface_flux,
    })
    out.to_csv(DATA_DIR / "photon_flux_toa_surface_280-500nm.csv", index=False)
    print(f"Saved {len(out)} points to photon_flux_toa_surface_280-500nm.csv")

    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.plot(df.wavelength_nm, toa_flux, color=COLORS[0], lw=LINEWIDTH, label="Top of atmosphere (AM0)")
    ax.plot(df.wavelength_nm, surface_flux, color=COLORS[1], lw=LINEWIDTH, label="Surface (AM1.5)")
    ax.set_yscale("log")
    ax.set_xlabel("Wavelength (nm)", fontsize=FONTSIZE)
    ax.set_ylabel("Photon flux (s$^{-1}$ cm$^{-2}$ nm$^{-1}$)", fontsize=FONTSIZE)
    ax.set_title("Solar photon flux, 280-500 nm", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.set_ylim(1e12, 1e15)
    ax.legend(fontsize=FONTSIZE - 3, loc="lower right")
    add_energy_axis(ax)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "photon_flux_toa_surface_280-500nm.png", dpi=150)
    print("Saved plot to photon_flux_toa_surface_280-500nm.png")


if __name__ == "__main__":
    main()
