"""
Solar Spectral Irradiance Plot
===============================
Reproduces the classic "solar spectrum with atmospheric absorption bands"
figure: the top-of-atmosphere curve (extraterrestrial, AM0), the
Earth's-surface curve after atmospheric absorption by O3, O2, H2O and CO2
(AM1.5 global), and a 5778 K blackbody curve for comparison.

Data: ASTM G173-03 reference spectra, data/astmg173.csv.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from _plot_style import FIGSIZE, LINEWIDTH, FONTSIZE, TITLE_FONTSIZE, COLORS, apply_style

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIGURES_DIR = REPO_ROOT / "assets" / "figures"

# ----------------------------------------------------------------------
# 1. Load ASTM G173 reference spectra
# ----------------------------------------------------------------------

df = pd.read_csv(DATA_DIR / "astmg173.csv")
df.columns = ["wavelength_nm", "extraterrestrial", "global_tilt", "direct_circumsolar"]

wavelength = df.wavelength_nm.to_numpy()
extraterrestrial = df.extraterrestrial.to_numpy()
terrestrial = df.global_tilt.to_numpy()

# ----------------------------------------------------------------------
# 2. 5778 K blackbody curve, for comparison with the measured AM0 curve
# ----------------------------------------------------------------------


def planck_spectral_radiance(wavelength_nm, T):
    """Spectral radiance of a blackbody, W / (m^2 sr nm)."""
    h = 6.62607015e-34  # Planck constant, J s
    c = 2.998e8  # speed of light, m/s
    k = 1.380649e-23  # Boltzmann constant, J/K

    wl_m = wavelength_nm * 1e-9
    numerator = 2 * h * c**2
    exponent = (h * c) / (wl_m * k * T)
    denom = wl_m**5 * (np.exp(exponent) - 1)
    radiance = numerator / denom  # W / (m^2 sr m)
    return radiance * 1e-9  # -> W / (m^2 sr nm)


def blackbody_irradiance(wavelength_nm, T=5778):
    """Blackbody curve scaled by the sun-to-earth solid angle to give
    irradiance at 1 AU, comparable to the AM0 curve."""
    radiance = planck_spectral_radiance(wavelength_nm, T)
    R_sun = 6.957e8
    d_sun_earth = 1.496e11
    omega = np.pi * (R_sun / d_sun_earth) ** 2
    return radiance * omega


blackbody = blackbody_irradiance(wavelength)

# ----------------------------------------------------------------------
# 3. Plot
# ----------------------------------------------------------------------

apply_style()
fig, ax = plt.subplots(figsize=FIGSIZE)

ax.plot(wavelength, extraterrestrial, color=COLORS[0], lw=LINEWIDTH, label="Top of atmosphere (AM0)")
ax.plot(wavelength, terrestrial, color=COLORS[1], lw=LINEWIDTH, label="Surface (AM1.5)")
ax.plot(wavelength, blackbody, color="grey", linestyle="--", lw=LINEWIDTH, label="5778 K blackbody")

# UV / Visible / Infrared region boundaries
ax.axvline(380, color="black", linestyle=":", linewidth=1)
ax.axvline(700, color="black", linestyle=":", linewidth=1)
ax.text(300, 2.35, "UV", fontsize=FONTSIZE - 2, ha="center")
ax.text(530, 2.35, "Visible", fontsize=FONTSIZE - 2, ha="center")
ax.text(900, 2.35, "Infrared", fontsize=FONTSIZE - 2, ha="left")

# Absorption-band labels (approximate positions/wavelengths)
label_style = dict(color="navy", fontsize=FONTSIZE - 3, fontweight="bold", ha="center")
ax.text(270, 0.05, "O$_3$", **label_style)
ax.text(760, 0.20, "O$_2$", **label_style)
ax.text(940, 0.10, "H$_2$O", **label_style)
ax.text(1130, 0.42, "H$_2$O", **label_style)
ax.text(1870, 0.22, "H$_2$O", **label_style)
ax.text(2500, 0.13, "H$_2$O", **label_style)
ax.text(2020, 0.05, "CO$_2$", **label_style)

# Axes formatting
ax.set_xlim(250, 2600)
ax.set_ylim(0, 2.5)
ax.set_xlabel("Wavelength (nm)", fontsize=FONTSIZE)
ax.set_ylabel("Spectral irradiance (W/m$^2$/nm)", fontsize=FONTSIZE)
ax.set_title("Solar spectral irradiance (ASTM G173)", fontsize=TITLE_FONTSIZE)
ax.tick_params(labelsize=FONTSIZE - 1)
ax.set_xticks(range(250, 2600, 500))

fig.tight_layout()
fig.savefig(FIGURES_DIR / "solar_spectrum.png", dpi=150)
print("Saved plot.")
