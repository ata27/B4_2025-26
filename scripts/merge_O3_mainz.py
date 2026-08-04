"""
Merge MPI-Mainz UV/VIS Spectral Atlas O3 cross-section files into a single
100-1000 nm dataset.

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python merge_O3_mainz.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, LEGEND_FONTSIZE, apply_style, add_energy_axis

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

BASE = "https://www.uv-vis-spectral-atlas-mainz.org/uvvis_data/cross_sections/Ozone/"

# Priority order: earlier entries win in overlapping regions.
FILES = [
    "O3_Mason(1996)_298K_110.2-337.4nm.txt",
    "O3_OgawaCook(1958)_295K_52-131nm.txt",
    "O3_Serdyuchenko(2014)_293K_213-1100nm(2013 version).txt",
]

WL_MIN, WL_MAX = 100.0, 1000.0  # nm, output plot/CSV range


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

    clipped.to_csv(DATA_DIR / "O3_merged_100-1000nm.csv", index=False)
    print(f"\nSaved {len(clipped)} points to O3_merged_100-1000nm.csv")

    # Plot
    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for src, grp in clipped.groupby("source"):
        ax.plot(grp.wavelength_nm, grp.cross_section_cm2, label=src, lw=LINEWIDTH)
    ax.set_yscale("log")
    ax.set_xlabel("Wavelength (nm)", fontsize=FONTSIZE)
    ax.set_ylabel("Cross section (cm$^2$/molecule)", fontsize=FONTSIZE)
    ax.set_title("O$_3$ UV/VIS absorption cross section, 100-1000 nm", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.legend(fontsize=LEGEND_FONTSIZE, loc="upper right")
    add_energy_axis(ax)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "O3_merged_100-1000nm.png", dpi=150)
    print("Saved plot to O3_merged_100-1000nm.png")


if __name__ == "__main__":
    main()
