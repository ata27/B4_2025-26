# data/

Reference datasets for use in the course notebooks.

## `us_standard_atmosphere_1976.csv`

The 1976 U.S. Standard Atmosphere reference profile, 0–86 km, computed at 0.5 km
resolution from the model's defining layer equations (base altitude, lapse rate and
base temperature per layer, integrated via the barometric/hydrostatic relation).

This is public-domain reference data. It was generated directly from the standard's
published layer definitions (not downloaded from a third party), so it's exactly
reproducible — see `scripts/generate_us_standard_atmosphere.py`.

**Columns:**

| Column | Description | Units |
|---|---|---|
| `altitude_km` | Altitude (geopotential height ≈ geometric height below ~50 km) | km |
| `temperature_K` | Temperature | K |
| `pressure_Pa` | Pressure | Pa |
| `density_kg_m3` | Mass density | kg m⁻³ |
| `number_density_cm3` | Number density [M] | molecules cm⁻³ |

**Validated** against the standard's published values at every layer boundary
(0, 11, 20, 32, 47, 51, 71, 84.852 km) to within 0.005%.

**Used in:**
- Module 1 notebook (`01-atmospheric-structure.ipynb`) — compare the scale-height/
  barometric-law approximation from Exercise 1 against the real (non-isothermal)
  standard atmosphere profile.
- Available to any other module — e.g. Module 3/4's Chapman-mechanism notebooks
  could use realistic T(z) instead of the simplified linear approximation currently
  used for `T_of_z()`.

**Loading it:**
```python
import pandas as pd
atm = pd.read_csv('../data/us_standard_atmosphere_1976.csv')
```
