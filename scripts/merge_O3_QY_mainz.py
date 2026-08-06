"""
Fetch the MPI-Mainz UV/VIS Spectral Atlas quantum yield files for the
O3 -> O(1D) + O2 photolysis channel at four temperatures and plot them
together.

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python merge_O3_QY_mainz.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style, add_energy_axis

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

BASE = "https://www.uv-vis-spectral-atlas-mainz.org/uvvis_data/quantum_yields/Ozone/"

DATASETS = {
    "203 K": "O3{O(1D)+O2}_Matsumi(2002)_203K_220-340nm.txt",
    "253 K": "O3{O(1D)+O2}_Matsumi(2002)_253K_220-340nm.txt",
    "298 K": "O3{O(1D)+O2}_Matsumi(2002)_298K_220-340nm.txt",
    "321 K": "O3{O(1D)+O2}_Matsumi(2002)_321K_220-340nm.txt",
}


def fetch_dataset(fname):
    url = BASE + requests.utils.quote(fname)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    rows = []
    for line in resp.text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        try:
            wl, qy = float(parts[0]), float(parts[1])
        except ValueError:
            continue
        rows.append((wl, qy))
    df = pd.DataFrame(rows, columns=["wavelength_nm", "quantum_yield"])
    df["source"] = fname
    return df.sort_values("wavelength_nm").reset_index(drop=True)


def main():
    temp_data = {}
    for temp, fname in DATASETS.items():
        print(f"Fetching {fname} ...")
        df = fetch_dataset(fname)
        print(f"  -> {len(df)} points, {df.wavelength_nm.min():.3f}-{df.wavelength_nm.max():.3f} nm")
        temp_data[temp] = df
        tag = temp.replace(" ", "")
        df.to_csv(DATA_DIR / f"O3_QY_O1D_{tag}.csv", index=False)
        print(f"  Saved {len(df)} points to O3_QY_O1D_{tag}.csv")

    # Plot
    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for color, (temp, df) in zip(COLORS, temp_data.items()):
        ax.plot(df.wavelength_nm, df.quantum_yield, color=color, lw=LINEWIDTH)
    ax.set_xlabel("Wavelength (nm)", fontsize=FONTSIZE)
    ax.set_ylabel("Quantum yield", fontsize=FONTSIZE)
    ax.set_title("O$_3$ $\\rightarrow$ O($^1$D) + O$_2$ quantum yield", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.set_ylim(0, 1.05)
    add_energy_axis(ax)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "O3_QY_O1D.png", dpi=150)
    print("Saved plot to O3_QY_O1D.png")


if __name__ == "__main__":
    main()
