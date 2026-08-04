# kinetic_data

Reaction and rate-coefficient data from Archibald et al. (2020, *GMD*),
*"Description and evaluation of the UKCA stratosphere-troposphere chemistry
scheme (StratTrop vn 1.0) implemented in UKESM1"*, Supplementary Information
Tables S1-S8.
https://doi.org/10.5194/gmd-13-1223-2020-supplement

| File | SI Table | Contents |
|---|---|---|
| `table_S1_bimolecular.csv` | S1 | Bi-molecular reactions: A, alpha, -Ea/R |
| `table_S2_termolecular.csv` | S2 | Termolecular (Troe-form) reactions: Fc, k1, k2 parameters |
| `table_S3_photolysis.csv` | S3 | Photodissociation reactions (reactants/products only; cross-sections in Telford et al. 2013) |
| `table_S4_heterogeneous.csv` | S4 | Heterogeneous reactions and uptake coefficients (liquid aerosol / NAT / ice) |
| `table_S5_aqueous_sulfur.csv` | S5 | Aqueous-phase sulfur cycle reactions with explicit rate expressions |
| `table_S6_henry_tropospheric.csv` | S6 | Henry's law + dissociation data, soluble tropospheric species |
| `table_S7_henry_stratospheric.csv` | S7 | Henry's law + dissociation data, soluble stratospheric species |
| `table_S8_henry_aerosol_precursor.csv` | S8 | Henry's law + dissociation data, aerosol precursor species |

`kinetics.py` provides functions to evaluate these:
- `load_table('S1'..'S8')`
- `k_bimolecular()`, `k_from_table_S1()` — Arrhenius rate coefficients (Table S1)
- `k_termolecular()`, `k_from_table_S2()` — Troe-form pressure-dependent rate coefficients (Table S2)
- `henry_constant()`, `effective_henry_constant()` — T-dependent Henry's law constants (Tables S6-S8)

**Sign convention note:** the SI's "-Ea/R" column must be *negated* in the
exponent to reproduce standard JPL/IUPAC rate coefficients, i.e.
`k = A*(T/300)^alpha*exp(-value/T)`. This has been verified against known
literature values (OH+CH4, Cl+CH4, BrO+NO) — see the docstring in
`kinetics.py` for details.

## Additional file (not from Archibald et al. 2020 SI)

| File | Contents |
|---|---|
| `voc_oxidation_kinetics.csv` | Rate constants (cm^3 molecule^-1 s^-1, single 298 K value, no T-dependence) for 44 VOCs against OH, O3, NO3, and Cl. Not all oxidant channels are reported for every compound (blank = no data / negligible channel). |

Use `voc_rate_constant(compound, oxidant)` in `kinetics.py` to look values up. Unlike Tables S1/S2, these are single reference-temperature values — `k_bimolecular()` (which needs A/alpha/-Ea/R) does not apply here.
