"""
Plot VOC oxidation rate constants and derived lifetimes vs carbon number,
in the house plot style used for the other lecture-note figures.

Data: assets/kinetic_data/voc_oxidation_kinetics.csv
    One row per compound, with rate constants (cm3 molecule-1 s-1) against
    up to four oxidants: OH, O3, NO3, Cl. Missing values are left blank.

Requires: pandas, matplotlib
    pip install pandas matplotlib

Run:
    python plot_voc_oxidation_kinetics.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, LogLocator

from _plot_style import LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style

SECONDS_PER_DAY = 86400.0

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "assets" / "kinetic_data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

DATA_FILE = "voc_oxidation_kinetics.csv"

# Rate-constant column, oxidant label, plot colour and typical ambient
# oxidant concentration (cm-3) used to convert k into a lifetime.
OXIDANTS = [
    ("kOH_cm3_molecule-1_s-1", "OH", COLORS[0], 1e6),
    ("kO3_cm3_molecule-1_s-1", "O$_3$", COLORS[1], 1e12),
    ("kNO3_cm3_molecule-1_s-1", "NO$_3$", COLORS[2], 2.5e7),
    ("kCl_cm3_molecule-1_s-1", "Cl", COLORS[3], 1e5),
]


def main():
    df = pd.read_csv(DATA_DIR / DATA_FILE)

    apply_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

    for col, label, color, conc in OXIDANTS:
        rates = df[col].to_numpy(dtype=float)
        mask = ~np.isnan(rates)
        carbon_number = df.loc[mask, "carbon_number"].to_numpy(dtype=float)
        k = rates[mask]

        ax1.scatter(
            carbon_number, np.log10(k),
            label=label, color=color, s=30, edgecolors="none",
        )

        lifetime_days = 1.0 / (k * conc) / SECONDS_PER_DAY
        ax2.scatter(
            carbon_number, lifetime_days,
            label=label, color=color, s=30, edgecolors="none",
        )

    ax1.set_xlabel("Carbon number", fontsize=FONTSIZE)
    ax1.set_ylabel("log$_{10}$(k / cm$^3$ molecule$^{-1}$ s$^{-1}$)", fontsize=FONTSIZE)
    ax1.tick_params(labelsize=FONTSIZE - 1)
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.grid(True, which="major", color="grey", alpha=0.4, lw=0.8)
    ax1.grid(True, which="minor", color="grey", alpha=0.2, lw=0.5)
    ax1.set_axisbelow(True)
    ax1.legend(fontsize=FONTSIZE - 2)

    ax2.set_xlabel("Carbon number", fontsize=FONTSIZE)
    ax2.set_ylabel("Lifetime (days)", fontsize=FONTSIZE)
    ax2.set_yscale("log")
    ax2.yaxis.set_major_locator(LogLocator(base=10.0, numticks=15))
    ax2.yaxis.set_minor_locator(LogLocator(base=10.0, subs=range(2, 10), numticks=15))
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.tick_params(labelsize=FONTSIZE - 1)
    ax2.grid(True, which="major", color="grey", alpha=0.4, lw=0.8)
    ax2.grid(True, which="minor", color="grey", alpha=0.2, lw=0.5)
    ax2.set_axisbelow(True)
    ax2.legend(fontsize=FONTSIZE - 2)

    fig.suptitle("VOC oxidation kinetics and lifetimes", fontsize=TITLE_FONTSIZE)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "voc_oxidation_kinetics_lifetimes.png", dpi=150)
    print("Saved plot to voc_oxidation_kinetics_lifetimes.png")


if __name__ == "__main__":
    main()
