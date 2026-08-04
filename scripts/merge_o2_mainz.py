"""
Merge MPI-Mainz UV/VIS Spectral Atlas O2 cross-section files into a single
50-250 nm dataset.

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python merge_o2_mainz.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, LEGEND_FONTSIZE, apply_style, add_energy_axis

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

BASE = "https://www.uv-vis-spectral-atlas-mainz.org/uvvis_data/cross_sections/Oxygen/"

# Priority order: earlier entries win in overlapping regions.
FILES = [
    "O2_Holland(1993)_298K_49-103nm.txt",
    "O2_Lee(1955)_295K_103.00-109.88nm.txt",
    "O2_OgawaOgawa(1975)_298K_108-160nm(X).txt",
    "O2_Hudson(1966)_300K_159-179nm.txt",
    "O2_Ackerman(1970)_300K_176-201nm.txt",
    "O2_Ogawa(1971)_298K_181-235nm.txt",
    "O2_ShardanandPrasadRao(1977)_300K_200-250nm.txt",
]

WL_MIN, WL_MAX = 50.0, 250.0  # nm, output plot/CSV range


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
    datasets = []
    for fname in FILES:
        print(f"Fetching {fname} ...")
        df = fetch_dataset(fname)
        print(f"  -> {len(df)} points, {df.wavelength_nm.min():.3f}-{df.wavelength_nm.max():.3f} nm")
        datasets.append(df)

    # Merge: keep points from higher-priority sources; only add points
    # from later sources that fall outside wavelengths already covered.
    merged = datasets[0].copy()
    for df in datasets[1:]:
        covered = (merged.wavelength_nm.min(), merged.wavelength_nm.max())
        # simple rule: only take points from this source that are NOT
        # within any already-covered source's native range
        existing_ranges = merged.groupby("source").wavelength_nm.agg(["min", "max"])
        mask = pd.Series(True, index=df.index)
        for _, (lo, hi) in existing_ranges.iterrows():
            mask &= ~df.wavelength_nm.between(lo, hi)
        merged = pd.concat([merged, df[mask]], ignore_index=True)

    merged = merged.sort_values("wavelength_nm").reset_index(drop=True)

    # Clip to requested plot range
    clipped = merged[(merged.wavelength_nm >= WL_MIN) & (merged.wavelength_nm <= WL_MAX)]

    clipped.to_csv(DATA_DIR / "O2_merged_50-250nm.csv", index=False)
    print(f"\nSaved {len(clipped)} points to O2_merged_50-250nm.csv")

    # Plot
    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for src, grp in clipped.groupby("source"):
        ax.plot(grp.wavelength_nm, grp.cross_section_cm2, label=src, lw=LINEWIDTH)
    ax.set_yscale("log")
    ax.set_xlabel("Wavelength (nm)", fontsize=FONTSIZE)
    ax.set_ylabel("Cross section (cm$^2$/molecule)", fontsize=FONTSIZE)
    ax.set_title("O$_2$ UV absorption cross section, 50-250 nm", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.legend(fontsize=LEGEND_FONTSIZE, loc="upper right")
    add_energy_axis(ax)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "O2_merged_50-250nm.png", dpi=150)
    print("Saved plot to O2_merged_50-250nm.png")


if __name__ == "__main__":
    main()
