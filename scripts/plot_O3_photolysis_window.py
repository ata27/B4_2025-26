"""
Plot the O3 Hartley-band photolysis window (290-340 nm): the O3
absorption cross section, the O3 -> O(1D) + O2 quantum yield, and the
scaled surface actinic photon flux, on a shared wavelength axis.

Reproduces (with real MPI-Mainz and ASTM G173 data, in the house plot
style) the classic "cross section / quantum yield / photon flux" figure
used to illustrate why J(O1D) is confined to this narrow window.

Data:
    data/O3_merged_100-1000nm.csv   (O3 cross section, MPI-Mainz)
    data/O3_QY_O1D_298K.csv         (O3 quantum yield, MPI-Mainz)
    data/astmg173.csv               (surface actinic flux, ASTM G173 AM1.5G)

Requires: pandas, matplotlib
    pip install pandas matplotlib

Run:
    python plot_O3_photolysis_window.py
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style, add_energy_axis

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

WL_MIN, WL_MAX = 290.0, 340.0  # nm

# Planck constant, speed of light (SI) - to convert irradiance to photon flux
_PLANCK = 6.62607015e-34  # J s
_LIGHTSPEED = 2.99792458e8  # m/s


def main():
    xs = pd.read_csv(DATA_DIR / "O3_merged_100-1000nm.csv")
    xs = xs[(xs.wavelength_nm >= WL_MIN) & (xs.wavelength_nm <= WL_MAX)]

    qy = pd.read_csv(DATA_DIR / "O3_QY_O1D_298K.csv")
    qy = qy[(qy.wavelength_nm >= WL_MIN) & (qy.wavelength_nm <= WL_MAX)]

    solar = pd.read_csv(DATA_DIR / "astmg173.csv")
    solar.columns = ["wavelength_nm", "extraterrestrial", "global_tilt", "direct_circumsolar"]
    solar = solar[(solar.wavelength_nm >= WL_MIN) & (solar.wavelength_nm <= WL_MAX)]

    # Convert surface irradiance (W/m^2/nm) to photon flux (photons/s/m^2/nm),
    # then scale to a peak of 1 over the plotted window.
    wl_m = solar.wavelength_nm.to_numpy() * 1e-9
    photon_energy = _PLANCK * _LIGHTSPEED / wl_m
    photon_flux = solar.global_tilt.to_numpy() / photon_energy
    photon_flux_scaled = photon_flux / photon_flux.max()

    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax2 = ax.twinx()

    ax.plot(qy.wavelength_nm, qy.quantum_yield, color=COLORS[1], lw=LINEWIDTH, label="Quantum yield")
    ax.plot(solar.wavelength_nm, photon_flux_scaled, color=COLORS[2], lw=LINEWIDTH, label="Photon flux (scaled)")
    ax2.plot(xs.wavelength_nm, xs.cross_section_cm2 * 1e18, color=COLORS[0], lw=LINEWIDTH, label="Cross section")

    ax.set_xlabel("Wavelength (nm)", fontsize=FONTSIZE)
    ax.set_ylabel("Scaled photon flux / quantum yield", fontsize=FONTSIZE - 1)
    ax2.set_ylabel("O$_3$ cross section (10$^{-18}$ cm$^2$)", fontsize=FONTSIZE)
    ax.set_title("O$_3$ photolysis window, 290-340 nm", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax2.tick_params(labelsize=FONTSIZE - 1)
    ax.set_xlim(WL_MIN, WL_MAX)
    ax.set_ylim(0, 1.05)
    ax2.set_ylim(bottom=0)

    lines = ax.get_lines() + ax2.get_lines()
    ax.legend(lines, [line.get_label() for line in lines], fontsize=FONTSIZE - 3, loc="upper right")

    add_energy_axis(ax)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "m7-fig2-2-o3-cross-section-qy-flux.png", dpi=150)
    print("Saved plot to m7-fig2-2-o3-cross-section-qy-flux.png")


if __name__ == "__main__":
    main()
