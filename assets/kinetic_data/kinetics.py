"""
kinetics.py
-----------
Helper functions for working with the UKCA StratTrop (vn1.0) reaction data
from Archibald et al. (2020, GMD), Tables S1-S8.

Data files expected in ./data/:
    table_S1_bimolecular.csv
    table_S2_termolecular.csv
    table_S3_photolysis.csv
    table_S4_heterogeneous.csv
    table_S5_aqueous_sulfur.csv
    table_S6_henry_tropospheric.csv
    table_S7_henry_stratospheric.csv
    table_S8_henry_aerosol_precursor.csv

All bimolecular/termolecular rate coefficients follow the Arrhenius form used
in the paper:

    k(T) = A * (T/300)^alpha * exp(-Ea_R / T)

For termolecular (pressure-dependent) reactions, the low- and high-pressure
limits k1(T), k2(T) are combined via the Troe expression given in the SI:

    k([M],T) = { k1[M] / (1 + k1[M]/k2) } * Fc ^ (1 / (1 + (log10(k1[M]/k2))^2))

Author: generated for lecture-note use alongside Archibald et al. (2020) SI.
"""

from __future__ import annotations
import os
import math
import numpy as np
import pandas as pd

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------
# Loading
# ----------------------------------------------------------------------

def load_table(name: str) -> pd.DataFrame:
    """Load one of the Table S1-S8 CSVs by short name, e.g. 'S1', 'S2', ...'S8'."""
    files = {
        "S1": "table_S1_bimolecular.csv",
        "S2": "table_S2_termolecular.csv",
        "S3": "table_S3_photolysis.csv",
        "S4": "table_S4_heterogeneous.csv",
        "S5": "table_S5_aqueous_sulfur.csv",
        "S6": "table_S6_henry_tropospheric.csv",
        "S7": "table_S7_henry_stratospheric.csv",
        "S8": "table_S8_henry_aerosol_precursor.csv",
        "VOC": "voc_oxidation_kinetics.csv",
    }
    key = name.upper().replace("TABLE_", "").strip()
    if key not in files:
        raise ValueError(f"Unknown table '{name}'. Choose from {list(files)}.")
    return pd.read_csv(os.path.join(DATA_DIR, files[key]))


# ----------------------------------------------------------------------
# Bimolecular rate law (Table S1)
# ----------------------------------------------------------------------

def k_bimolecular(A: float, alpha: float, neg_Ea_R: float, T):
    """
    Arrhenius rate coefficient used throughout Table S1:
        k(T) = A * (T/300)^alpha * exp(-neg_Ea_R / T)

    NOTE ON SIGN CONVENTION: the SI's 'neg_Ea_R' column (labelled "-Ea/R" in
    the PDF) is tabulated in the standard JPL/IUPAC style where the printed
    number must still be *negated* in the exponent (e.g. OH + CH4 has
    neg_Ea_R = +1775, and the well-known rate law is
    k = 2.45e-12 * exp(-1775/T), giving k(298K) ~ 6.3e-15 cm3/molec/s,
    matching the literature). This has been verified against known rate
    coefficients (OH+CH4, Cl+CH4, BrO+NO) - do not remove the minus sign.

    T may be a scalar or numpy array (K). Returns k in cm^3 molecule^-1 s^-1.
    """
    T = np.asarray(T, dtype=float)
    return A * (T / 300.0) ** alpha * np.exp(-neg_Ea_R / T)


def k_from_table_S1(df: pd.DataFrame, reactants: str, T, which: int = 0):
    """
    Convenience: look up a reaction in the Table S1 dataframe by its
    'reactants' string (e.g. 'OH + CH4') and evaluate k(T).
    If multiple rows match (branching reactions), `which` selects the row.
    """
    matches = df[df["reactants"].str.strip() == reactants.strip()].reset_index(drop=True)
    if matches.empty:
        raise KeyError(f"No reaction found with reactants '{reactants}'")
    row = matches.iloc[which]
    return k_bimolecular(row["A"], row["alpha"], row["neg_Ea_R"], T), row


# ----------------------------------------------------------------------
# Termolecular / Troe rate law (Table S2)
# ----------------------------------------------------------------------

def k_termolecular(Fc, k1_A, k1_alpha, k1_beta, k2_A, k2_alpha, k2_beta, T, M):
    """
    Troe-form termolecular rate coefficient, following the SI formulation:

        k1(T)  = k1_A * (T/300)^k1_alpha * exp(-k1_beta/T)      [low-pressure, cm^6 molecule^-2 s^-1]
        k2(T)  = k2_A * (T/300)^k2_alpha * exp(-k2_beta/T)      [high-pressure, cm^3 molecule^-1 s^-1]
        k([M],T) = ( k1[M] / (1 + k1[M]/k2) ) * Fc^(1/(1+(log10(k1[M]/k2))^2))

    T : temperature (K), scalar or array
    M : number density of air (molecule cm^-3), scalar or array
    Returns k in cm^3 molecule^-1 s^-1.
    """
    T = np.asarray(T, dtype=float)
    M = np.asarray(M, dtype=float)

    k1 = k1_A * (T / 300.0) ** k1_alpha * np.exp(-k1_beta / T)
    k2 = k2_A * (T / 300.0) ** k2_alpha * np.exp(-k2_beta / T)

    if Fc == 0:
        # Purely low-pressure-limited reactions in the table (Fc = 0.00)
        return k1 * M

    ratio = k1 * M / k2
    exponent = 1.0 / (1.0 + (np.log10(ratio)) ** 2)
    return (ratio / (1.0 + ratio)) * k2 * Fc ** exponent


def k_from_table_S2(df: pd.DataFrame, reactants: str, T, M):
    """Look up a Table S2 reaction by its 'reactants' string and evaluate k([M],T)."""
    row = df[df["reactants"].str.strip() == reactants.strip()]
    if row.empty:
        raise KeyError(f"No reaction found with reactants '{reactants}'")
    row = row.iloc[0]
    k = k_termolecular(row["Fc"], row["k1_A"], row["k1_alpha"], row["k1_beta"],
                        row["k2_A"], row["k2_alpha"], row["k2_beta"], T, M)
    return k, row


# ----------------------------------------------------------------------
# Effective Henry's law coefficient (Tables S6-S8)
# ----------------------------------------------------------------------

def henry_constant(KH_298, neg_dH_R, T):
    """
    van't-Hoff-style temperature dependence used for Henry's law constants:
        KH(T) = KH(298) * exp( -dH/R * (1/T - 1/298) )
    Here neg_dH_R is the tabulated '-dH/R' value (K), consistent with the SI.
    """
    T = np.asarray(T, dtype=float)
    return KH_298 * np.exp(neg_dH_R * (1.0 / T - 1.0 / 298.0))


def effective_henry_constant(KH_298, neg_dH_R, Ka_298, neg_dH_R_dissoc, T, pH=None, H_plus=None):
    """
    Effective (pH-dependent) Henry's law constant for a weak acid HA that
    partially dissociates in the aqueous phase:
        KH_eff(T) = KH(T) * (1 + Ka(T)/[H+])
    Provide either pH or H_plus (mol/L). If neither given, returns the
    non-dissociated KH(T).
    """
    KH_T = henry_constant(KH_298, neg_dH_R, T)
    if Ka_298 == 0 or (pH is None and H_plus is None):
        return KH_T
    Ka_T = henry_constant(Ka_298, neg_dH_R_dissoc, T)  # same van't Hoff form
    if H_plus is None:
        H_plus = 10 ** (-pH)
    return KH_T * (1.0 + Ka_T / H_plus)


# ----------------------------------------------------------------------
# US Standard Atmosphere (simplified) — altitude -> T, P, number density M
# ----------------------------------------------------------------------

_R = 8.31446   # J/mol/K
_g0 = 9.80665  # m/s^2
_M_air = 0.0289644  # kg/mol
_Na = 6.02214076e23  # molecules/mol

# Layer base altitudes (m), base T (K), base P (Pa), lapse rate (K/m)
_LAYERS = [
    (0.0,     288.15, 101325.0,  -0.0065),
    (11000.0, 216.65,  22632.06,  0.0),
    (20000.0, 216.65,   5474.89,  0.001),
    (32000.0, 228.65,    868.02,  0.0028),
    (47000.0, 270.65,    110.91,  0.0),
    (51000.0, 270.65,     66.94, -0.0028),
    (71000.0, 214.65,      3.96, -0.002),
    (84852.0, 186.87,      0.3734, 0.0),
]


def standard_atmosphere(z_m):
    """
    Simplified 1976 US Standard Atmosphere, valid 0-86 km.
    z_m : altitude in metres (scalar or array)
    Returns (T [K], P [Pa], M [molecule cm^-3])
    """
    z_m = np.atleast_1d(np.asarray(z_m, dtype=float))
    T_out = np.zeros_like(z_m)
    P_out = np.zeros_like(z_m)

    for i, z in enumerate(z_m):
        # find layer
        for j in range(len(_LAYERS) - 1, -1, -1):
            zb, Tb, Pb, L = _LAYERS[j]
            if z >= zb:
                break
        dz = z - zb
        if abs(L) < 1e-12:
            T = Tb
            P = Pb * math.exp(-_g0 * _M_air * dz / (_R * Tb))
        else:
            T = Tb + L * dz
            P = Pb * (T / Tb) ** (-_g0 * _M_air / (_R * L))
        T_out[i] = T
        P_out[i] = P

    # number density: M = P / (k_B T), convert to molecule/cm^3
    k_B = 1.380649e-23
    M_out = P_out / (k_B * T_out) * 1e-6  # molecule cm^-3

    if T_out.size == 1:
        return T_out[0], P_out[0], M_out[0]
    return T_out, P_out, M_out


# ----------------------------------------------------------------------
# VOC oxidant rate constants (single-T, reported at 298 K; voc_oxidation_kinetics.csv)
# ----------------------------------------------------------------------

def voc_rate_constant(compound: str, oxidant: str = "OH"):
    """
    Look up the reported (298 K) bimolecular rate constant for a VOC + oxidant
    reaction from voc_oxidation_kinetics.csv.

    compound : e.g. 'C2H6', 'APINENE', 'Toluene' (matches the 'compound' column)
    oxidant  : one of 'OH', 'O3', 'NO3', 'Cl'

    Returns k in cm^3 molecule^-1 s^-1, or None if no rate constant is
    reported for that oxidant (many alkanes have no O3/NO3 channel, and
    most alkenes/aromatics have no reported Cl rate here).

    NOTE: unlike Tables S1/S2 (Arrhenius/Troe parameters valid over a T
    range), this file gives single rate constants only (298 K reference,
    no temperature dependence) -- do not use k_bimolecular() on these.
    """
    df = load_table("VOC")
    col = f"k{oxidant}_cm3_molecule-1_s-1"
    if col not in df.columns:
        raise ValueError(f"Unknown oxidant '{oxidant}'. Choose from OH, O3, NO3, Cl.")
    row = df[df["compound"].str.strip() == compound.strip()]
    if row.empty:
        raise KeyError(f"No VOC entry found for compound '{compound}'")
    val = row.iloc[0][col]
    return None if pd.isna(val) else float(val)
