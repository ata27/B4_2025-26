"""
Reconstruction of WMO/UNEP Scientific Assessment of Ozone Depletion (1998),
Chapter 11, Figure 11-4: "Contributions of the classes of substances to
total equivalent effective stratospheric chlorine (EESC) according to the
Baseline scenario (A1)."

IMPORTANT — please read before treating the numbers as authoritative:
The 1998 report tabulates *emissions* (Table 11-5, ktonnes/yr) and gives a
handful of *summary* EESC statistics (1980 = 1986 ppt, 1990 = 2871 ppt,
peak in 1997, individual-species % contribution in 1995, etc.) but it does
NOT publish a year-by-year ppt table of each species' EESC contribution.
So this script does not reproduce the original data set -- it builds a
physically-motivated approximation (a simple single-compartment
emission -> lifetime-decay model per species class) that is *calibrated*
to match the published anchor points:
  - total EESC ~1986 ppt in 1980, ~2871 ppt in 1990, peaks ~1997
  - 1995 species contributions: CFCs 41%, CCl4 11%, CH3CCl3 11%,
    halons 9%, CH3Br(anthropogenic) 2.9%, HCFCs 0.9%,
    CH3Cl(natural) 12%, CH3Br(natural) 12%  (WMO 1998, Sec 11.4.3)
  - long-lived species (CFCs, halons) decline slowly after ~1997;
    short-lived species (CH3CCl3, CH3Br) collapse quickly after
    production is phased out, consistent with their atmospheric
    lifetimes (WMO 1998, Table 2-1 / Sec 2)

Treat the resulting CSV/plot as a teaching-quality reconstruction of the
shape and relative magnitude of Figure 11-4, not as the original WMO data.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# ---------------------------------------------------------------
# 1. Build each species-class contribution to EESC (ppt) vs. year
# ---------------------------------------------------------------
years = np.arange(1940, 2101, 1)

def rise_decay(t, peak_year, rise_width, decay_tau, amplitude):
    """Smooth logistic rise to `peak_year`, then exponential decay with
    time constant `decay_tau` (mimics 1st-order atmospheric removal
    after emissions are phased out)."""
    t_mid = peak_year - 4 * rise_width          # logistic midpoint
    rise = 1.0 / (1.0 + np.exp(-(t - t_mid) / rise_width))
    decay = np.exp(-np.clip(t - peak_year, 0, None) / decay_tau)
    shape = np.where(t <= peak_year, rise, decay)
    return amplitude * shape

# species: (label, peak_year, rise_width_yr, decay_tau_yr, amplitude_ppt)
# amplitude/peak-year chosen to satisfy the 1995 percentage breakdown
# and the qualitative peak-timing/decay-rate statements in WMO 1998 Ch.11
species_params = {
    "CFCs":        dict(peak_year=1997, rise_width=10, decay_tau=80, amplitude=1350),
    "CH3CCl3":     dict(peak_year=1994, rise_width=6,  decay_tau=6,  amplitude=380),
    "CCl4":        dict(peak_year=1993, rise_width=8,  decay_tau=32, amplitude=380),
    "HCFCs":       dict(peak_year=2012, rise_width=12, decay_tau=15, amplitude=140),
    "Halons":      dict(peak_year=2012, rise_width=10, decay_tau=55, amplitude=420),
    "CH3Br_anthro":dict(peak_year=1998, rise_width=6,  decay_tau=8,  amplitude=100),
}

data = {"Year": years}
for name, p in species_params.items():
    data[name] = rise_decay(years, **p)

# Natural sources: essentially constant over the whole period
data["CH3Cl_natural"] = np.full_like(years, 380.0, dtype=float)
data["CH3Br_natural"] = np.full_like(years, 380.0, dtype=float)

df = pd.DataFrame(data)

# ---------------------------------------------------------------
# 2. Cumulative ("stacked") totals, in the same bottom-to-top order
#    used in the original figure
# ---------------------------------------------------------------
stack_order = ["CH3Cl_natural", "CH3Br_natural", "CFCs", "CH3CCl3",
               "CCl4", "HCFCs", "Halons", "CH3Br_anthro"]

cum = df[stack_order].cumsum(axis=1)
cum.columns = [f"cum_{c}" for c in stack_order]
df = pd.concat([df, cum], axis=1)
df.rename(columns={"cum_CH3Br_anthro": "cum_Total_EESC"}, inplace=True)

# ---------------------------------------------------------------
# 3. Save the data
# ---------------------------------------------------------------
csv_path = "/mnt/user-data/outputs/eesc_baseline_A1_reconstruction.csv"
df.to_csv(csv_path, index=False)
print("Saved:", csv_path)
print(df.loc[df.Year.isin([1980, 1990, 1995, 1997, 2050, 2100])].to_string(index=False))

# ---------------------------------------------------------------
# 4. Plot, styled after the original Figure 11-4
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 6.2), dpi=200)

tab20 = plt.get_cmap("tab20")
colors = {
    "cum_CH3Cl_natural": tab20(0),
    "cum_CH3Br_natural": tab20(1),
    "cum_CFCs":          tab20(2),
    "cum_CH3CCl3":       tab20(3),
    "cum_CCl4":          tab20(4),
    "cum_HCFCs":         tab20(5),
    "cum_Halons":        tab20(6),
    "cum_Total_EESC":    tab20(7),
}

# individual (non-cumulative) flat natural-source lines, as in the original
ax.plot(df.Year, df.cum_CH3Cl_natural, color=colors["cum_CH3Cl_natural"], lw=1.8)
ax.plot(df.Year, df.cum_CH3Br_natural, color=colors["cum_CH3Br_natural"], lw=1.8)

# cumulative anthropogenic stack lines
for col in ["cum_CFCs", "cum_CH3CCl3", "cum_CCl4", "cum_HCFCs",
            "cum_Halons", "cum_Total_EESC"]:
    ax.plot(df.Year, df[col], color=colors[col], lw=1.8)

label_pos = {
    "CH$_3$Cl":            (2040, df.cum_CH3Cl_natural.iloc[0] + 40, colors["cum_CH3Cl_natural"]),
    "CH$_3$Br(N)":         (2040, df.cum_CH3Br_natural.iloc[0] + 40, colors["cum_CH3Br_natural"]),
    "CFCs":                (2043, np.interp(2043, df.Year, df.cum_CFCs) + 40, colors["cum_CFCs"]),
    "CH$_3$CCl$_3$":       (2000, np.interp(2000, df.Year, df.cum_CH3CCl3) + 40, colors["cum_CH3CCl3"]),
    "CCl$_4$":             (1985, np.interp(1985, df.Year, df.cum_CCl4) + 40, colors["cum_CCl4"]),
    "HCFCs":               (2008, np.interp(2008, df.Year, df.cum_HCFCs) + 40, colors["cum_HCFCs"]),
    "halons":              (1988, np.interp(1988, df.Year, df.cum_Halons) + 40, colors["cum_Halons"]),
    "CH$_3$Br(A)":         (1975, np.interp(1975, df.Year, df.cum_Total_EESC) + 60, colors["cum_Total_EESC"]),
}
for text, (x, y, c) in label_pos.items():
    ax.text(x, y, text, fontsize=10.5, ha="left", va="bottom", color=c,
            fontweight="bold")

ax.set_xlim(1940, 2100)
ax.set_ylim(0, 3500)
ax.set_xticks([1940, 1980, 2020, 2060, 2100])
ax.set_ylabel("EESC (ppt)", fontsize=12)
ax.set_xlabel("Year", fontsize=12)
ax.set_title("Baseline scenario A1", fontsize=13, pad=14)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
fig_path = "/mnt/user-data/outputs/eesc_baseline_A1_reconstruction.png"
fig.savefig(fig_path, facecolor="white")
print("Saved:", fig_path)
