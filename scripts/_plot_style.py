"""
Shared plotting helpers for the MPI-Mainz photolysis cross-section scripts.

Keeps figure size, font sizes, line widths and the wavelength <-> photon
energy secondary axis consistent across all merge_*_mainz.py scripts.
"""

FIGSIZE = (6, 4)  # inches (width, height) - fits ~A4 lecture notes
LINEWIDTH = 2.0
FONTSIZE = 12
TITLE_FONTSIZE = 10
LEGEND_FONTSIZE = 9

# E (kJ/mol) = N_A * h * c / wavelength, with wavelength in nm
_PLANCK = 6.62607015e-34  # J s
_LIGHTSPEED = 2.99792458e8  # m/s
_AVOGADRO = 6.02214076e23  # 1/mol
_KJ_PER_MOL_NM = _PLANCK * _LIGHTSPEED * _AVOGADRO * 1e9 / 1e3


def wavelength_nm_to_energy_kJmol(wavelength_nm):
    return _KJ_PER_MOL_NM / wavelength_nm


def energy_kJmol_to_wavelength_nm(energy_kJmol):
    return _KJ_PER_MOL_NM / energy_kJmol


def apply_style():
    import matplotlib.pyplot as plt

    plt.rcParams.update({"font.size": FONTSIZE})


def add_energy_axis(ax):
    secax = ax.secondary_xaxis(
        "top",
        functions=(wavelength_nm_to_energy_kJmol, energy_kJmol_to_wavelength_nm),
    )
    secax.set_xlabel("Photon energy (kJ/mol)", fontsize=FONTSIZE)
    secax.tick_params(labelsize=FONTSIZE - 1)
    return secax
