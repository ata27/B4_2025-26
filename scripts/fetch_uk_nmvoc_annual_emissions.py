"""
Fetch UK NMVOC (non-methane volatile organic compound) annual emissions
data from the UK government's "Emissions of air pollutants" statistics
release, and plot the 1970-2024 time series (cf. Figure 10 in the
official release).

Data source:
    https://www.gov.uk/government/statistics/emissions-of-air-pollutants/
    emissions-of-air-pollutants-in-the-uk-non-methane-volatile-organic-
    compounds-nmvocs

Requires: requests, pandas, matplotlib
    pip install requests pandas matplotlib

Run:
    python fetch_uk_nmvoc_annual_emissions.py
"""

from pathlib import Path

import requests
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

URL = "https://assets.publishing.service.gov.uk/media/698328ec20fe1bb69ac243cb/fig10_nmvoc_annual_emissions.csv"


def main():
    print(f"Fetching {URL} ...")
    resp = requests.get(URL, timeout=30)
    resp.raise_for_status()

    out_csv = DATA_DIR / "uk_nmvoc_annual_emissions_1970-2024.csv"
    out_csv.write_bytes(resp.content)
    df = pd.read_csv(out_csv)
    df.columns = ["series", "year", "emissions_Mt"]
    print(f"  -> {len(df)} points, series: {sorted(df.series.unique())}")
    print(f"Saved to {out_csv.name}")

    # The source file bundles four series: the main historical emissions
    # trend, an alternative "NECR" reporting-basis series (National
    # Emission Ceilings Regulations), and two flat 2020-2029 target/
    # ceiling reference lines (ERC, CLRTAP) -- matching the official
    # Figure 10. The NECR series is omitted from the plot below.
    main = df[df.series == "Non Methane VOC"]
    erc = df[df.series == "erc_2020-2029"]
    clrtap = df[df.series == "clrtap_2020-2029"]

    # Plot
    apply_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.plot(main.year, main.emissions_Mt, color=COLORS[0], lw=LINEWIDTH, label="NMVOC emissions")
    ax.plot(erc.year, erc.emissions_Mt, color=COLORS[1], lw=LINEWIDTH, linestyle=":", label="Emission Reduction Commitment")
    ax.plot(clrtap.year, clrtap.emissions_Mt, color=COLORS[2], lw=LINEWIDTH, linestyle=":", label="CLRTAP ceiling")
    ax.set_xlabel("Year", fontsize=FONTSIZE)
    ax.set_ylabel("NMVOC emissions (Mt)", fontsize=FONTSIZE)
    ax.set_title("UK annual NMVOC emissions, 1970-2024", fontsize=TITLE_FONTSIZE)
    ax.tick_params(labelsize=FONTSIZE - 1)
    ax.set_ylim(bottom=0)
    ax.legend(fontsize=FONTSIZE - 4, loc="upper right")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "uk_nmvoc_annual_emissions.png", dpi=150)
    print("Saved plot to uk_nmvoc_annual_emissions.png")


if __name__ == "__main__":
    main()
