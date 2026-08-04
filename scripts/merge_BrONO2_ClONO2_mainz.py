"""
Fetch the MPI-Mainz UV/VIS Spectral Atlas BrONO2 and ClONO2 cross-section
files (both at 298 K) and plot them together.

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python merge_BrONO2_ClONO2_mainz.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

BASE = "https://www.uv-vis-spectral-atlas-mainz.org/uvvis_data/cross_sections/Halogenated%20N-compounds(inorg)/"

DATASETS = {
    "BrONO2": "BrONO2_JPL-2010(2011)_298K_200-500nm(rec).txt",
    "ClONO2": "ClONO2_JPL-2010(2011)_298K_196-432nm(rec).txt",
}


def fetch_dataset(fname):
    url = BASE + fname
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
            wl, xs = float(parts[0]), float(parts[1])
        except ValueError:
            continue
        rows.append((wl, xs))
    df = pd.DataFrame(rows, columns=["wavelength_nm", "cross_section_cm2"])
    df["source"] = fname
    return df.sort_values("wavelength_nm").reset_index(drop=True)


def main():
    species_data = {}
    for species, fname in DATASETS.items():
        print(f"Fetching {fname} ...")
        df = fetch_dataset(fname)
        print(f"  -> {len(df)} points, {df.wavelength_nm.min():.3f}-{df.wavelength_nm.max():.3f} nm")
        species_data[species] = df
        df.to_csv(DATA_DIR / f"{species}_298K.csv", index=False)
        print(f"  Saved {len(df)} points to {species}_298K.csv")

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    for species, df in species_data.items():
        ax.plot(df.wavelength_nm, df.cross_section_cm2, label=species, lw=1)
    ax.set_yscale("log")
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Cross section (cm$^2$/molecule)")
    ax.set_title("BrONO$_2$ and ClONO$_2$ UV absorption cross sections, 298 K (MPI-Mainz)")
    ax.legend(fontsize=9, loc="upper right")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "BrONO2_ClONO2_298K.png", dpi=150)
    print("Saved plot to BrONO2_ClONO2_298K.png")


if __name__ == "__main__":
    main()
