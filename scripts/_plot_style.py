"""
Shared plotting helpers for the MPI-Mainz photolysis cross-section scripts.

Keeps figure size, font sizes, line widths and the wavelength <-> photon
energy secondary axis consistent across all merge_*_mainz.py scripts.
"""

FIGSIZE = (6, 4)  # inches (width, height) - fits ~A4 lecture notes
LINEWIDTH = 2.0
FONTSIZE = 12
TITLE_FONTSIZE = 10

# Colour per curve, keyed by how many species/curves share one plot.
COLORS = ["black", "orange", "blue", "green", "red"]

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


def add_energy_axis(ax, n_ticks=5):
    """
    Add a secondary top x-axis showing photon energy (kJ/mol).

    Energy is a 1/wavelength function, so ticks placed at "nice" energy
    values bunch together in pixel space at the short-wavelength end.
    Instead, ticks are chosen evenly spaced in wavelength (i.e. evenly
    spaced in pixels along the shared axis) and labelled with their
    corresponding energy.
    """
    secax = ax.secondary_xaxis(
        "top",
        functions=(wavelength_nm_to_energy_kJmol, energy_kJmol_to_wavelength_nm),
    )
    secax.set_xlabel("Photon energy (kJ/mol)", fontsize=FONTSIZE)
    secax.tick_params(labelsize=FONTSIZE - 1)

    xmin, xmax = ax.get_xlim()
    step = (xmax - xmin) / (n_ticks - 1)
    wavelengths = [xmin + i * step for i in range(n_ticks)]
    energies = [wavelength_nm_to_energy_kJmol(w) for w in wavelengths]
    secax.set_xticks(energies)
    secax.set_xticklabels([f"{e:.0f}" for e in energies])
    return secax
