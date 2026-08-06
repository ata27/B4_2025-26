"""
Plot the A -> B -> C chain reaction (Module 2, Chemical Kinetics notes),
comparing the exact solution for [B] against the steady-state
approximation [B]_ss = k1[A]/k2, for two (k1, k2) pairs.

    d[A]/dt = -k1[A]
    d[B]/dt = k1[A] - k2[B]
    d[C]/dt = k2[B]

Solved analytically (closed form for a linear first-order chain), so no
numerical ODE integration is required:

    [A](t) = A0 exp(-k1 t)
    [B](t) = k1 A0 / (k2 - k1) * (exp(-k1 t) - exp(-k2 t))
    [C](t) = A0 - [A](t) - [B](t)

Reproduces the A->B->C figure from notebooks/02-chemical-kinetics.ipynb,
in the house plot style used elsewhere in the course repo.

Requires: numpy, matplotlib
    pip install numpy matplotlib

Run:
    python plot_abc_chain.py
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from _plot_style import LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style

REPO_ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

A0 = 1.0
K_PAIRS = [(1, 2), (1, 10)]  # (k1, k2), s^-1


def abc_chain(t, k1, k2, A0=1.0):
    A = A0 * np.exp(-k1 * t)
    B = k1 * A0 / (k2 - k1) * (np.exp(-k1 * t) - np.exp(-k2 * t))
    C = A0 - A - B
    return A, B, C


def main():
    t = np.linspace(0, 8, 400)

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(9, 4), sharey=True)

    for ax, (k1, k2) in zip(axes, K_PAIRS):
        A, B, C = abc_chain(t, k1, k2, A0)
        B_ss = k1 * A / k2

        ax.plot(t, A, color=COLORS[0], lw=LINEWIDTH, label="[A]")
        ax.plot(t, B, color=COLORS[1], lw=LINEWIDTH, label="[B]")
        ax.plot(t, B_ss, color=COLORS[1], lw=LINEWIDTH, linestyle="--", label="[B]$_{ss}$")
        ax.plot(t, C, color=COLORS[2], lw=LINEWIDTH, label="[C]")
        ax.set_xlabel("Time (s)", fontsize=FONTSIZE)
        ax.set_title(f"k$_1$={k1}, k$_2$={k2} s$^{{-1}}$", fontsize=TITLE_FONTSIZE)
        ax.tick_params(labelsize=FONTSIZE - 1)

    axes[0].set_ylabel("Concentration (arb. units)", fontsize=FONTSIZE)
    axes[1].legend(fontsize=FONTSIZE - 3, loc="upper right")

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "m2-fig-abc-chain.png", dpi=150)
    print("Saved plot to m2-fig-abc-chain.png")


if __name__ == "__main__":
    main()
