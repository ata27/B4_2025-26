"""
Fetch the MPI-Mainz UV/VIS Spectral Atlas NO2 cross-section file and save
it as a 240-662.5 nm dataset at 294 K.

The source file bins each cross section over a wavelength range
("lo-hi") rather than giving a single wavelength, so each bin is
represented here by its midpoint.

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python merge_NO2_mainz.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

BASE = "https://www.uv-vis-spectral-atlas-mainz.org/uvvis_data/cross_sections/Nitrogen%20oxides/"

FNAME = "NO2_JPL-2010(2011)_294K_240-662.5nm(rec).txt"

WL_MIN, WL_MAX = 240.0, 662.5  # nm, output plot/CSV range


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
        wl_part, xs_part = parts
        try:
            xs = float(xs_part)
        except ValueError:
            continue
        if "-" in wl_part:
            lo, hi = wl_part.split("-")
            try:
                wl = (float(lo) + float(hi)) / 2
            except ValueError:
                continue
        else:
            try:
                wl = float(wl_part)
            except ValueError:
                continue
        rows.append((wl, xs))
    df = pd.DataFrame(rows, columns=["wavelength_nm", "cross_section_cm2"])
    df["source"] = fname
    return df.sort_values("wavelength_nm").reset_index(drop=True)


def main():
    print(f"Fetching {FNAME} ...")
    df = fetch_dataset(FNAME)
    print(f"  -> {len(df)} points, {df.wavelength_nm.min():.3f}-{df.wavelength_nm.max():.3f} nm")

    clipped = df[(df.wavelength_nm >= WL_MIN) & (df.wavelength_nm <= WL_MAX)]

    clipped.to_csv(DATA_DIR / "NO2_merged_240-662.5nm.csv", index=False)
    print(f"\nSaved {len(clipped)} points to NO2_merged_240-662.5nm.csv")

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    for src, grp in clipped.groupby("source"):
        ax.plot(grp.wavelength_nm, grp.cross_section_cm2, label=src, lw=1)
    ax.set_yscale("log")
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Cross section (cm$^2$/molecule)")
    ax.set_title("NO$_2$ UV/VIS absorption cross section, 240-662.5 nm, 294 K (MPI-Mainz)")
    ax.legend(fontsize=7, loc="upper right")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "NO2_merged_240-662.5nm.png", dpi=150)
    print("Saved plot to NO2_merged_240-662.5nm.png")


if __name__ == "__main__":
    main()
