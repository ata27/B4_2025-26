"""
Fetch the MPI-Mainz UV/VIS Spectral Atlas cross-section files for
CFC-11, CFC-12 and CFC-13 (most up-to-date JPL recommendations) and
plot them together.

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python merge_CFC_mainz.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style, add_energy_axis

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

BASE = (
    "https://www.uv-vis-spectral-atlas-mainz.org/uvvis_data/cross_sections/"
    "Halogeno-alkanes%2Bradicals/Freons-CFC(C,F,Cl)/"
)

# Most up-to-date JPL recommendation available for each species.
# CFC-13 has no JPL-2015 entry, so JPL-2010 is the latest available.
DATASETS = {
    "CFC-11": "CFCl3(CFC-11)_JPL-2015(2015)_298K_174-260nm(rec).txt",
    "CFC-12": "CF2Cl2(CFC-12)_JPL-2015(2015)_298K_170-240nm(rec).txt",
    "CFC-13": "CF3Cl(CFC-13)_JPL-2010(2011)_296K_172-220nm(rec).txt",
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
        df.to_csv(DATA_DIR / f"{species.replace('-', '')}_298K.csv", index=False)
        print(f"  Saved {len(df)} points to {species.replace('-', '')}_298K.csv")

    # Plot
    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for color, (species, df) in zip(COLORS, species_data.items()):
        ax.plot(df.wavelength_nm, df.cross_section_cm2, color=color, lw=LINEWIDTH)
    ax.set_yscale("log")
    ax.set_xlabel("Wavelength (nm)", fontsize=FONTSIZE)
    ax.set_ylabel("Cross section (cm$^2$/molecule)", fontsize=FONTSIZE)
    ax.set_title("CFC-11, CFC-12 and CFC-13 UV absorption cross sections", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    add_energy_axis(ax)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "CFC-11_12_13_298K.png", dpi=150)
    print("Saved plot to CFC-11_12_13_298K.png")


if __name__ == "__main__":
    main()
