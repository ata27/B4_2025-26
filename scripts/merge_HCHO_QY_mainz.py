"""
Fetch the MPI-Mainz UV/VIS Spectral Atlas quantum yield files for the two
HCHO (CH2O) photolysis channels (H2 + CO, and H + HCO) at 300 K and plot
them together.

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python merge_HCHO_QY_mainz.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style, add_energy_axis

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

BASE = "https://www.uv-vis-spectral-atlas-mainz.org/uvvis_data/quantum_yields/Organics%20(carbonyls)/Aldehydes(aliphatic)/"

DATASETS = {
    "H2 + CO": "CH2O{H2+CO}_Roeth(2015)_300K_250-360nm.txt",
    "H + HCO": "CH2O{H+HCO}_Roeth(2015)_300K_250-360nm.txt",
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
    channel_data = {}
    for channel, fname in DATASETS.items():
        print(f"Fetching {fname} ...")
        df = fetch_dataset(fname)
        print(f"  -> {len(df)} points, {df.wavelength_nm.min():.3f}-{df.wavelength_nm.max():.3f} nm")
        channel_data[channel] = df
        tag = channel.replace(" ", "").replace("+", "")
        df.to_csv(DATA_DIR / f"HCHO_QY_{tag}_300K.csv", index=False)
        print(f"  Saved {len(df)} points to HCHO_QY_{tag}_300K.csv")

    # Plot
    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for color, (channel, df) in zip(COLORS, channel_data.items()):
        ax.plot(df.wavelength_nm, df.quantum_yield, color=color, lw=LINEWIDTH)
    ax.set_xlabel("Wavelength (nm)", fontsize=FONTSIZE)
    ax.set_ylabel("Quantum yield", fontsize=FONTSIZE)
    ax.set_title("HCHO photolysis quantum yields, 300 K", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.set_ylim(0, 1.05)
    add_energy_axis(ax)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "HCHO_QY_300K.png", dpi=150)
    print("Saved plot to HCHO_QY_300K.png")


if __name__ == "__main__":
    main()
