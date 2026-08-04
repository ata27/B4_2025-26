"""
Fetch the MPI-Mainz UV/VIS Spectral Atlas HCHO (formaldehyde, CH2O)
cross-section file and save it as a 226-375 nm dataset at 298 K.

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python merge_HCHO_mainz.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

BASE = "https://www.uv-vis-spectral-atlas-mainz.org/uvvis_data/cross_sections/Organics%20(carbonyls)/Aldehydes(aliphatic)/"

FNAME = "CH2O_JPL-2015(2015)_298K_226-375nm(rec,1nm).txt"

WL_MIN, WL_MAX = 226.0, 375.0  # nm, output plot/CSV range


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
        if len(parts) < 2:
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
    print(f"Fetching {FNAME} ...")
    df = fetch_dataset(FNAME)
    print(f"  -> {len(df)} points, {df.wavelength_nm.min():.3f}-{df.wavelength_nm.max():.3f} nm")

    clipped = df[(df.wavelength_nm >= WL_MIN) & (df.wavelength_nm <= WL_MAX)]

    clipped.to_csv(DATA_DIR / "HCHO_merged_226-375nm.csv", index=False)
    print(f"\nSaved {len(clipped)} points to HCHO_merged_226-375nm.csv")

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    for src, grp in clipped.groupby("source"):
        ax.plot(grp.wavelength_nm, grp.cross_section_cm2, label=src, lw=1)
    ax.set_yscale("log")
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Cross section (cm$^2$/molecule)")
    ax.set_title("HCHO UV absorption cross section, 226-375 nm, 298 K (MPI-Mainz)")
    ax.legend(fontsize=7, loc="upper right")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "HCHO_merged_226-375nm.png", dpi=150)
    print("Saved plot to HCHO_merged_226-375nm.png")


if __name__ == "__main__":
    main()
