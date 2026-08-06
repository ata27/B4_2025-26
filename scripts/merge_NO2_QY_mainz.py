"""
Fetch the MPI-Mainz UV/VIS Spectral Atlas quantum yield files for the
NO2 -> NO + O(3P) photolysis channel at two temperatures and plot them
together.

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python merge_NO2_QY_mainz.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style, add_energy_axis

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

BASE = "https://www.uv-vis-spectral-atlas-mainz.org/uvvis_data/quantum_yields/Nitrogen%20oxides/"

DATASETS = {
    "248 K": "NO2{NO+O(3P)}_Troe(2000)_248K_300-415nm.txt",
    "298 K": "NO2{NO+O(3P)}_Troe(2000)_298K_300-415nm.txt",
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
        df.to_csv(DATA_DIR / f"NO2_QY_NO_O3P_{tag}.csv", index=False)
        print(f"  Saved {len(df)} points to NO2_QY_NO_O3P_{tag}.csv")

    # Plot
    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for color, (temp, df) in zip(COLORS, temp_data.items()):
        ax.plot(df.wavelength_nm, df.quantum_yield, color=color, lw=LINEWIDTH)
    ax.set_xlabel("Wavelength (nm)", fontsize=FONTSIZE)
    ax.set_ylabel("Quantum yield", fontsize=FONTSIZE)
    ax.set_title("NO$_2$ $\\rightarrow$ NO + O($^3$P) quantum yield", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.set_ylim(0, 1.05)
    add_energy_axis(ax)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "NO2_QY_NO_O3P.png", dpi=150)
    print("Saved plot to NO2_QY_NO_O3P.png")


if __name__ == "__main__":
    main()
