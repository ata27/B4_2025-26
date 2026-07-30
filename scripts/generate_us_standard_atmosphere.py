"""
Generate the 1976 U.S. Standard Atmosphere reference profile (0-86 km), using the
standard layer definitions (NOAA/NASA/USAF, 1976).

Public-domain reference data, computed directly from the model's defining equations
(not downloaded from any source), so it's exactly reproducible. Altitude is geopotential
height (the model's native coordinate) -- this differs from geometric altitude by less
than 0.1% below 50 km, so for teaching purposes the two are used interchangeably.
"""
import numpy as np
import csv

g0 = 9.80665       # m/s^2, standard gravity
R = 8.31432        # J/(mol K), gas constant used in the 1976 standard
M = 0.0289644      # kg/mol, mean molar mass of air

# (base altitude [m], lapse rate [K/m], base temperature [K])
layers = [
    (0,      -0.0065, 288.15),
    (11000,   0.0,     216.65),
    (20000,   0.0010,  216.65),
    (32000,   0.0028,  228.65),
    (47000,   0.0,     270.65),
    (51000,  -0.0028,  270.65),
    (71000,  -0.0020,  214.65),
    (84852,   0.0,     186.946),
]
P0 = 101325.0  # Pa, sea-level base pressure

def layer_base_pressures(layers, P0):
    pressures = [P0]
    for i in range(len(layers) - 1):
        h0, L, T0 = layers[i]
        h1 = layers[i + 1][0]
        P_prev = pressures[-1]
        if L == 0.0:
            P_next = P_prev * np.exp(-g0 * M * (h1 - h0) / (R * T0))
        else:
            T1 = T0 + L * (h1 - h0)
            P_next = P_prev * (T1 / T0) ** (-g0 * M / (R * L))
        pressures.append(P_next)
    return pressures

base_pressures = layer_base_pressures(layers, P0)

def atmosphere_at(h_m):
    """Return (T [K], P [Pa]) at a given altitude in metres (0-86000 m)."""
    idx = 0
    for i, (h0, L, T0) in enumerate(layers):
        if h_m >= h0:
            idx = i
        else:
            break
    h0, L, T0 = layers[idx]
    P0_layer = base_pressures[idx]
    if L == 0.0:
        T = T0
        P = P0_layer * np.exp(-g0 * M * (h_m - h0) / (R * T0))
    else:
        T = T0 + L * (h_m - h0)
        P = P0_layer * (T / T0) ** (-g0 * M / (R * L))
    return T, P

rows = []
for z_km in np.arange(0, 86.001, 0.5):
    T, P = atmosphere_at(z_km * 1000)
    rho = P * M / (R * T)
    n_cm3 = (P / (1.380649e-23 * T)) * 1e-6
    rows.append((round(z_km, 1), round(T, 3), round(P, 5), round(rho, 8), f"{n_cm3:.6e}"))

with open('/home/claude/course/data/us_standard_atmosphere_1976.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['altitude_km', 'temperature_K', 'pressure_Pa', 'density_kg_m3', 'number_density_cm3'])
    writer.writerows(rows)

checks = {0: (288.15, 101325), 11: (216.65, 22632), 20: (216.65, 5474.9),
          32: (228.65, 868.02), 47: (270.65, 110.91), 51: (270.65, 66.94),
          71: (214.65, 3.9564), 84.852: (186.946, 0.3734)}
print("Sanity check vs known reference values:")
max_err = 0
for z_km, (T_ref, P_ref) in checks.items():
    T, P = atmosphere_at(z_km * 1000)
    t_err = abs(T - T_ref)
    p_err = abs(P - P_ref) / P_ref * 100
    max_err = max(max_err, t_err, p_err)
    print(f"  {z_km:7.3f} km: T={T:8.3f} K (ref {T_ref:8.3f}, diff {t_err:.4f}),  "
          f"P={P:10.4f} Pa (ref {P_ref:10.4f}, diff {p_err:.4f}%)")

print(f"\nMax discrepancy: {max_err:.4f} -- should be ~0 (exact by construction)")
print(f"Table written: {len(rows)} rows, 0-86 km at 0.5 km resolution")
