"""
Plot photolysis (J) rates vs altitude, in the house plot style used for the
other lecture-note figures.

Data: data/j_rates_20151222_00z_40N_0E.csv
    Rows are variables (day of year, altitude, species J rates, ...),
    columns are model levels, so the file is transposed before use.

Requires: pandas, matplotlib
    pip install pandas matplotlib

Run:
    python plot_j_rates_altitude.py
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator

from _plot_style import LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, apply_style


def _j_to_tau(j_rate):
    return 1.0 / j_rate


def _tau_to_j(tau):
    return 1.0 / tau

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

DATA_FILE = "j_rates_20151222_00z_40N_0E.csv"

NON_SPECIES_ROWS = {
    "day of year", "hour of day", "altitude km", "latitude", "longitude",
    "cloud fraction", "pressure Pa", "cos SZA rad", "up SW flux",
    "down SW flux", "temperature K", "ozone column DU",
}

# Fixed colour per species: the 8-hue validated categorical palette (chosen
# in fixed CVD-safe order), plus black for the 9th species since there are
# more species here than the palette's slots.
SPECIES_COLORS = [
    "#2a78d6",  # blue
    "#eb6834",  # orange
    "#1baf7a",  # aqua
    "#eda100",  # yellow
    "#e87ba4",  # magenta
    "#008300",  # green
    "#4a3aa7",  # violet
    "#e34948",  # red
    "#000000",  # black (9th species, outside the 8-slot palette)
]


def main():
    raw = pd.read_csv(DATA_DIR / DATA_FILE, index_col=0)
    altitude_km = raw.loc["altitude km"].to_numpy(dtype=float)
    species_rows = [
        name for name in raw.index
        if name not in NON_SPECIES_ROWS and (raw.loc[name].to_numpy(dtype=float) > 0).any()
    ]

    apply_style()
    fig, ax = plt.subplots(figsize=(9, 5))

    for i, species in enumerate(species_rows):
        j_rate = raw.loc[species].to_numpy(dtype=float)
        ax.plot(
            j_rate, altitude_km,
            label=species,
            color=SPECIES_COLORS[i % len(SPECIES_COLORS)],
            lw=LINEWIDTH,
        )

    ax.set_xscale("log")
    ax.set_xlabel("J rate (s$^{-1}$)", fontsize=FONTSIZE)
    ax.set_ylabel("Altitude (km)", fontsize=FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.set_ylim(0, altitude_km.max())
    # H2O photolysis is negligible below the mesopause (down to ~1e-37 s^-1);
    # clip the axis so the tropospheric/stratospheric species stay legible.
    ax.set_xlim(1e-12, 1e-1)
    ax.xaxis.set_major_locator(LogLocator(base=10.0, numticks=15))
    ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs=range(2, 10), numticks=15))
    ax.legend(fontsize=FONTSIZE - 3, loc="upper left")

    secax = ax.secondary_xaxis("top", functions=(_j_to_tau, _tau_to_j))
    secax.set_xlabel(r"Lifetime $\tau = 1/J$ (s)", fontsize=FONTSIZE)
    secax.tick_params(labelsize=FONTSIZE - 1)
    secax.xaxis.set_major_locator(LogLocator(base=10.0, numticks=15))

    fig.suptitle("Photolysis rates, 40°N 0°E, 22 Dec 2015 00Z", fontsize=TITLE_FONTSIZE)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "j_rates_altitude_profile.png", dpi=150)
    print("Saved plot to j_rates_altitude_profile.png")


if __name__ == "__main__":
    main()
