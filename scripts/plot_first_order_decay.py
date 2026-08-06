"""
Plot first-order decay of [A] for several rate coefficients k, in the
house plot style used elsewhere in the course repo.

Reproduces Fig 2.1 from the Module 2 (Chemical Kinetics) notes /
notebook (notebooks/02-chemical-kinetics.ipynb).

Requires: numpy, matplotlib
    pip install numpy matplotlib

Run:
    python plot_first_order_decay.py
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style

REPO_ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

K_VALUES = [0.5, 1, 2, 4]  # s^-1
A0 = 1.0


def main():
    t = np.linspace(0, 5, 200)

    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for color, k in zip(COLORS, K_VALUES):
        ax.plot(t, A0 * np.exp(-k * t), color=color, lw=LINEWIDTH, label=f"k = {k} s$^{{-1}}$")

    ax.set_xlabel("Time (s)", fontsize=FONTSIZE)
    ax.set_ylabel("[A]/[A]$_0$", fontsize=FONTSIZE)
    ax.set_title("First-order decay", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.legend(fontsize=FONTSIZE - 3, loc="upper right")

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "m2-fig2-1-first-order-decay.png", dpi=150)
    print("Saved plot to m2-fig2-1-first-order-decay.png")


if __name__ == "__main__":
    main()
