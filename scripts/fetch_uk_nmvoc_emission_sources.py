"""
Fetch UK NMVOC emissions by source-sector data from the UK government's
"Emissions of air pollutants" statistics release (cf. Figure 11 in the
official release), and plot each source's fractional contribution to
total UK NMVOC emissions across the available years (1990, 2005, 2023,
2024).

Data source:
    https://www.gov.uk/government/statistics/emissions-of-air-pollutants/
    emissions-of-air-pollutants-in-the-uk-non-methane-volatile-organic-
    compounds-nmvocs

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python fetch_uk_nmvoc_emission_sources.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, FONTSIZE, TITLE_FONTSIZE, apply_style

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

URL = "https://assets.publishing.service.gov.uk/media/698329135a7e802e96d343c7/fig11_nmvoc_key_emission_sources.csv"


def main():
    print(f"Fetching {URL} ...")
    resp = requests.get(URL, timeout=30)
    resp.raise_for_status()

    out_csv = DATA_DIR / "uk_nmvoc_emission_sources_1990-2024.csv"
    out_csv.write_bytes(resp.content)
    df = pd.read_csv(out_csv)
    df.columns = ["source", "year", "emissions_Mt"]
    print(f"  -> {len(df)} points, sources: {sorted(df.source.unique())}")
    print(f"Saved to {out_csv.name}")

    # Fractional contribution of each source to the reported total, per year
    totals = df[df.source == "Total"].set_index("year").emissions_Mt
    sources = df[df.source != "Total"]
    pivot = sources.pivot(index="year", columns="source", values="emissions_Mt")
    fraction = pivot.div(totals, axis=0) * 100

    frac_out = DATA_DIR / "uk_nmvoc_emission_source_fractions_1990-2024.csv"
    fraction.to_csv(frac_out)
    print(f"Saved source fractions to {frac_out.name}")

    # Plot: stacked bars showing composition of total NMVOC emissions by source
    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    years = fraction.index.to_numpy()
    source_colors = plt.get_cmap("tab10").colors
    bottom = None
    for color, source in zip(source_colors, fraction.columns):
        values = fraction[source].to_numpy()
        ax.bar(years.astype(str), values, bottom=bottom, color=color, label=source, width=0.6)
        bottom = values if bottom is None else bottom + values

    ax.set_xlabel("Year", fontsize=FONTSIZE)
    ax.set_ylabel("Share of total NMVOC emissions (%)", fontsize=FONTSIZE)
    ax.set_title("UK NMVOC emissions by source", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.set_ylim(0, 100)
    ax.legend(fontsize=FONTSIZE - 4, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "uk_nmvoc_emission_sources.png", dpi=150)
    print("Saved plot to uk_nmvoc_emission_sources.png")


if __name__ == "__main__":
    main()
