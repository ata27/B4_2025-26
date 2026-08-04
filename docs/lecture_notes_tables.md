# UKCA StratTrop vn1.0 Reaction Data (Archibald et al., 2020, GMD)

Source: *Description and evaluation of the UKCA stratosphere-troposphere chemistry scheme (StratTrop vn 1.0) implemented in UKESM1*, Supplementary Information, Tables S1-S8. https://doi.org/10.5194/gmd-13-1223-2020-supplement

Machine-readable versions of these tables (CSV) and a Python module () for evaluating rate coefficients are provided alongside this document.

## Table S1. Bi-molecular reactions

| reactants       | products                                                                                                           |        A |   alpha |   neg_Ea_R | water_or_pressure_dependent   |
|:----------------|:-------------------------------------------------------------------------------------------------------------------|---------:|--------:|-----------:|:------------------------------|
| Br + Cl2O2      | BrCl + Cl + O2                                                                                                     | 5.9e-12  |    0    |        170 | nan                           |
| Br + HCHO       | HBr + CO + HO2                                                                                                     | 1.7e-11  |    0    |        800 | nan                           |
| Br + HO2        | HBr + O2                                                                                                           | 4.8e-12  |    0    |        310 | nan                           |
| Br + O3         | BrO + O2                                                                                                           | 1.6e-11  |    0    |        780 | nan                           |
| Br + OClO       | BrO + ClO                                                                                                          | 2.6e-11  |    0    |       1300 | nan                           |
| BrO + BrO       | Br + Br + O2                                                                                                       | 2.4e-12  |    0    |        -40 | nan                           |
| BrO + ClO       | Br + Cl + O2                                                                                                       | 2.3e-12  |    0    |       -260 | nan                           |
| BrO + ClO       | Br + OClO                                                                                                          | 9.5e-13  |    0    |       -550 | nan                           |
| BrO + ClO       | BrCl + O2                                                                                                          | 4.1e-13  |    0    |       -290 | nan                           |
| BrO + HO2       | HOBr + O2                                                                                                          | 4.5e-12  |    0    |       -460 | nan                           |
| BrO + NO        | Br + NO2                                                                                                           | 8.8e-12  |    0    |       -260 | nan                           |
| BrO + OH        | Br + HO2                                                                                                           | 1.7e-11  |    0    |       -250 | nan                           |
| CF2Cl2 + O(1D)  | Cl + ClO                                                                                                           | 1.4e-10  |    0    |          0 | nan                           |
| CFCl3 + O(1D)   | Cl + Cl + ClO                                                                                                      | 2.3e-10  |    0    |          0 | nan                           |
| Cl + CH4        | HCl + MeOO                                                                                                         | 7.3e-12  |    0    |       1280 | nan                           |
| Cl + Cl2O2      | Cl + Cl + Cl                                                                                                       | 7.6e-11  |    0    |        -65 | nan                           |
| Cl + ClONO2     | Cl + Cl + NO3                                                                                                      | 6.5e-12  |    0    |       -135 | nan                           |
| Cl + H2         | HCl + H                                                                                                            | 3.05e-11 |    0    |       2270 | nan                           |
| Cl + H2O2       | HCl + HO2                                                                                                          | 1.1e-11  |    0    |        980 | nan                           |
| Cl + HCHO       | HCl + CO + HO2                                                                                                     | 8.1e-11  |    0    |         30 | nan                           |
| Cl + HO2        | ClO + OH                                                                                                           | 3.65e-11 |    0    |        375 | nan                           |
| Cl + HO2        | HCl + O2                                                                                                           | 1.4e-11  |    0    |       -270 | nan                           |
| Cl + HOCl       | Cl + Cl + OH                                                                                                       | 3.4e-12  |    0    |        130 | nan                           |
| Cl + NO3        | ClO + NO2                                                                                                          | 2.4e-11  |    0    |          0 | nan                           |
| Cl + O3         | ClO + O2                                                                                                           | 2.3e-11  |    0    |        200 | nan                           |
| Cl + OClO       | ClO + ClO                                                                                                          | 3.4e-11  |    0    |       -160 | nan                           |
| Cl + MeOOH      | HCl + MeOO                                                                                                         | 5.7e-11  |    0    |          0 | nan                           |
| ClO + ClO       | Cl + Cl + O2                                                                                                       | 1e-12    |    0    |       1590 | nan                           |
| ClO + ClO       | Cl + Cl + O2                                                                                                       | 3e-11    |    0    |       2450 | nan                           |
| ClO + ClO       | Cl + OClO                                                                                                          | 3.5e-13  |    0    |       1370 | nan                           |
| ClO + HO2       | HOCl + O2                                                                                                          | 2.6e-12  |    0    |       -290 | nan                           |
| ClO + MeOO      | Cl + HCHO + HO2                                                                                                    | 3.3e-12  |    0    |        115 | nan                           |
| ClO + NO        | Cl + NO2                                                                                                           | 6.4e-12  |    0    |       -290 | nan                           |
| ClO + NO3       | Cl + O2 + NO2                                                                                                      | 4.6e-13  |    0    |          0 | nan                           |
| EtCO3 + NO      | EtOO + CO2 + NO2                                                                                                   | 6.7e-12  |    0    |       -340 | nan                           |
| EtCO3 + NO3     | EtOO + CO2 + NO2                                                                                                   | 4e-12    |    0    |          0 | nan                           |
| EtOO + MeCO3    | MeCHO + HO2 + MeOO                                                                                                 | 4.4e-13  |    0    |      -1070 | nan                           |
| EtOO + NO       | MeCHO + HO2 + NO2                                                                                                  | 2.55e-12 |    0    |       -380 | nan                           |
| EtOO + NO3      | MeCHO + HO2 + NO2                                                                                                  | 2.3e-12  |    0    |          0 | nan                           |
| H + HO2         | H2 + O2                                                                                                            | 6.9e-12  |    0    |          0 | nan                           |
| H + HO2         | O(3P) + H2O                                                                                                        | 1.62e-12 |    0    |          0 | nan                           |
| H + HO2         | OH + OH                                                                                                            | 7.2e-11  |    0    |          0 | nan                           |
| H + NO2         | OH + NO                                                                                                            | 4e-10    |    0    |        340 | nan                           |
| H + O3          | OH + O2                                                                                                            | 1.4e-10  |    0    |        470 | nan                           |
| HO2 + HO2       | H2O2                                                                                                               | 3e-13    |    0    |       -460 | water_dependent               |
| HO2 + MeOO      | MeOOH                                                                                                              | 3.8e-13  |    0    |       -780 | water_dependent               |
| HO2 + NO        | OH + NO2                                                                                                           | 3.3e-12  |    0    |       -270 | nan                           |
| HO2 + NO3       | OH + NO2 + O2                                                                                                      | 3.5e-12  |    0    |          0 | nan                           |
| HO2 + O3        | OH + O2 + O2                                                                                                       | 2.03e-16 |    4.57 |       -693 | nan                           |
| HO2 + EtCO3     | O2 + EtCO3H                                                                                                        | 4.4e-13  |    0    |       -980 | nan                           |
| HO2 + EtCO3     | O3 + EtCO2H                                                                                                        | 7.8e-14  |    0    |       -980 | nan                           |
| HO2 + EtOO      | EtOOH                                                                                                              | 6.4e-13  |    0    |       -710 | nan                           |
| HO2 + ISO2      | ISOOH                                                                                                              | 2.05e-13 |    0    |      -1300 | nan                           |
| HO2 + MACRO2    | MACROOH                                                                                                            | 1.82e-13 |    0    |      -1300 | nan                           |
| HO2 + MeCO3     | MeCO2H + O3                                                                                                        | 7.8e-14  |    0    |       -980 | nan                           |
| HO2 + MeCO3     | MeCO3H                                                                                                             | 2.13e-13 |    0    |       -980 | nan                           |
| HO2 + MeCO3     | OH + MeOO                                                                                                          | 2.29e-13 |    0    |       -980 | nan                           |
| HO2 + MeCOCH2OO | MeCOCH2OOH                                                                                                         | 9e-12    |    0    |          0 | nan                           |
| HO2 + MeOO      | HCHO                                                                                                               | 3.8e-13  |    0    |       -780 | water_dependent               |
| HO2 + i-PrOO    | i-PrOOH                                                                                                            | 1.51e-13 |    0    |      -1300 | nan                           |
| HO2 + n-PrOO    | n-PrOOH                                                                                                            | 1.51e-13 |    0    |      -1300 | nan                           |
| i-PrOO + NO     | Me2CO + HO2 + NO2                                                                                                  | 2.7e-12  |    0    |       -360 | nan                           |
| i-PrOO + NO3    | Me2CO + HO2 + NO2                                                                                                  | 2.7e-12  |    0    |       -360 | nan                           |
| ISO2 + ISO2     | MACR + MACR + HCHO + HO2                                                                                           | 2e-12    |    0    |          0 | nan                           |
| MACRO2 + MACRO2 | HACET + MGLY + 0.5*HCHO + 0.5*CO + HO2                                                                             | 2e-12    |    0    |          0 | nan                           |
| MeBr + Cl       | Br + HCl                                                                                                           | 1.4e-11  |    0    |       1030 | nan                           |
| MeBr + O(1D)    | Br + OH                                                                                                            | 1.8e-10  |    0    |          0 | nan                           |
| MeBr + OH       | Br + H2O                                                                                                           | 2.35e-12 |    0    |       1300 | nan                           |
| MeCO3 + NO      | MeOO + CO2 + NO2                                                                                                   | 7.5e-12  |    0    |       -290 | nan                           |
| MeCO3 + NO3     | MeOO + CO2 + NO2                                                                                                   | 4e-12    |    0    |          0 | nan                           |
| MeCOCH2OO + NO  | MeCO3 + HCHO + NO2                                                                                                 | 2.7e-12  |    0    |       -360 | nan                           |
| MeCOCH2OO + NO3 | MeCO3 + HCHO + NO2                                                                                                 | 2.3e-12  |    0    |          0 | nan                           |
| MeOO + NO       | HO2 + HCHO + NO2                                                                                                   | 2.3e-12  |    0    |       -360 | nan                           |
| MeOO + MeOO     | HO2 + HO2 + HCHO + HCHO                                                                                            | 1.03e-13 |    0    |       -365 | nan                           |
| MeOO + MeCO3    | HO2 + HCHO + MeOO                                                                                                  | 1.8e-12  |    0    |       -500 | nan                           |
| MeOO + MeCO3    | MeCO2H + HCHO                                                                                                      | 2e-13    |    0    |       -500 | nan                           |
| MeOO + MeOO     | MeOH + HCHO                                                                                                        | 1.03e-13 |    0    |       -365 | nan                           |
| MeOO + NO       | MeONO2                                                                                                             | 2.3e-15  |    0    |       -360 | nan                           |
| MeOO + NO3      | HO2 + HCHO + NO2                                                                                                   | 1.2e-12  |    0    |          0 | nan                           |
| N + NO          | N2 + O(3P)                                                                                                         | 2.1e-11  |    0    |       -100 | nan                           |
| N + NO2         | N2O + O(3P)                                                                                                        | 5.8e-12  |    0    |       -220 | nan                           |
| N + O2          | NO + O(3P)                                                                                                         | 1.5e-11  |    0    |       3600 | nan                           |
| n-PrOO + NO     | EtCHO + HO2 + NO2                                                                                                  | 2.9e-12  |    0    |       -350 | nan                           |
| n-PrOO + NO3    | EtCHO + HO2 + NO2                                                                                                  | 2.7e-12  |    0    |       -360 | nan                           |
| N2O5 + H2O      | HONO2 + HONO2                                                                                                      | 2.5e-22  |    0    |          0 | nan                           |
| NO + NO3        | NO2 + NO2                                                                                                          | 1.5e-11  |    0    |       -170 | nan                           |
| NO + O3         | NO2                                                                                                                | 3e-12    |    0    |       1500 | nan                           |
| NO + ISO2       | ISON                                                                                                               | 1.12e-13 |    0    |       -360 | nan                           |
| NO + ISO2       | NO2 + MACR + HCHO + HO2                                                                                            | 2.43e-12 |    0    |       -360 | nan                           |
| NO + MACRO2     | NO2 + 0.25*MeCO3 + 0.25*HACET + 0.25*CO + 0.5*MGLY + 0.75*HCHO + 0.75*HO2                                          | 2.54e-12 |    0    |       -360 | nan                           |
| NO2 + NO3       | NO + NO2 + O2                                                                                                      | 4.5e-14  |    0    |       1260 | nan                           |
| NO2 + O3        | NO3                                                                                                                | 1.2e-13  |    0    |       2450 | nan                           |
| NO3 + Br        | BrO + NO2                                                                                                          | 1.6e-11  |    0    |          0 | nan                           |
| NO3 + HCHO      | HONO2 + HO2 + CO                                                                                                   | 2e-12    |    0    |       2440 | nan                           |
| NO3 + C5H8      | ISON                                                                                                               | 3.15e-12 |    0    |        450 | nan                           |
| NO3 + EtCHO     | HONO2 + EtCO3                                                                                                      | 6.3e-15  |    0    |          0 | nan                           |
| NO3 + MGLY      | MeCO3 + CO + HONO2                                                                                                 | 3.36e-12 |    0    |       1860 | nan                           |
| NO3 + Me2CO     | HONO2 + MeCOCH2OO                                                                                                  | 3e-17    |    0    |          0 | nan                           |
| NO3 + MeCHO     | HONO2 + MeCO3                                                                                                      | 1.4e-12  |    0    |       1860 | nan                           |
| O(1D) + CH4     | HCHO + H2                                                                                                          | 9e-12    |    0    |          0 | nan                           |
| O(1D) + CH4     | OH + MeOO                                                                                                          | 1.31e-10 |    0    |          0 | nan                           |
| O(1D) + CO2     | O(3P) + CO2                                                                                                        | 7.5e-11  |    0    |       -115 | nan                           |
| O(1D) + H2      | OH + H                                                                                                             | 1.2e-10  |    0    |          0 | nan                           |
| O(1D) + H2O     | OH + OH                                                                                                            | 1.63e-10 |    0    |        -60 | nan                           |
| O(1D) + HBr     | HBr + O(3P)                                                                                                        | 3e-11    |    0    |          0 | nan                           |
| O(1D) + HBr     | OH + Br                                                                                                            | 1.2e-10  |    0    |          0 | nan                           |
| O(1D) + HCl     | H + ClO                                                                                                            | 3.6e-11  |    0    |          0 | nan                           |
| O(1D) + HCl     | O(3P) + HCl                                                                                                        | 1.35e-11 |    0    |          0 | nan                           |
| O(1D) + HCl     | OH + Cl                                                                                                            | 1.01e-10 |    0    |          0 | nan                           |
| O(1D) + N2      | O(3P) + N2                                                                                                         | 2.15e-11 |    0    |       -110 | nan                           |
| O(1D) + N2O     | N2 + O2                                                                                                            | 4.6e-11  |    0    |        -20 | nan                           |
| O(1D) + N2O     | NO + NO                                                                                                            | 7.3e-11  |    0    |        -20 | nan                           |
| O(1D) + O2      | O(3P) + O2                                                                                                         | 3.3e-11  |    0    |        -55 | nan                           |
| O(1D) + O3      | O2 + O(3P) + O(3P)                                                                                                 | 1.2e-10  |    0    |          0 | nan                           |
| O(1D) + O3      | O2 + O2                                                                                                            | 1.2e-10  |    0    |          0 | nan                           |
| O(1D) + CH4     | HCHO + HO2 + HO2                                                                                                   | 3.45e-11 |    0    |          0 | nan                           |
| O(3P) + BrO     | O2 + Br                                                                                                            | 1.9e-11  |    0    |       -230 | nan                           |
| O(3P) + ClO     | Cl + O2                                                                                                            | 2.8e-11  |    0    |        -85 | nan                           |
| O(3P) + ClONO2  | ClO + NO3                                                                                                          | 3.6e-12  |    0    |        840 | nan                           |
| O(3P) + H2      | OH + H                                                                                                             | 9e-18    |    0    |          0 | nan                           |
| O(3P) + H2O2    | OH + HO2                                                                                                           | 1.4e-12  |    0    |       2000 | nan                           |
| O(3P) + HBr     | OH + Br                                                                                                            | 5.8e-12  |    0    |       1500 | nan                           |
| O(3P) + HCHO    | OH + CO + HO2                                                                                                      | 3.4e-11  |    0    |       1600 | nan                           |
| O(3P) + HCl     | OH + Cl                                                                                                            | 1e-11    |    0    |       3300 | nan                           |
| O(3P) + HO2     | OH + O2                                                                                                            | 2.7e-11  |    0    |       -224 | nan                           |
| O(3P) + HOCl    | OH + ClO                                                                                                           | 1.7e-13  |    0    |          0 | nan                           |
| O(3P) + NO2     | NO + O2                                                                                                            | 5.1e-12  |    0    |       -210 | nan                           |
| O(3P) + NO3     | O2 + NO2                                                                                                           | 1.7e-11  |    0    |          0 | nan                           |
| O(3P) + O3      | O2 + O2                                                                                                            | 8e-12    |    0    |       2060 | nan                           |
| O(3P) + OClO    | O2 + ClO                                                                                                           | 2.4e-12  |    0    |        960 | nan                           |
| O(3P) + OH      | O2 + H                                                                                                             | 1.8e-11  |    0    |       -180 | nan                           |
| O3 + C5H8       | 0.25*HO2 + 0.25*OH + 0.65*MACR + 0.58*HCHO + 0.1*MACRO2 + 0.1*MeCO3 + 0.08*MeOO + 0.28*HCOOH + 0.14*CO + 0.09*H2O2 | 9.99e-15 |    0    |       1995 | nan                           |
| O3 + MACR       | 0.9*MGLY + 0.45*HCOOH + 0.32*HO2 + 0.22*CO + 0.19*OH + 0.1*MeCO3                                                   | 4.26e-16 |    0    |       1520 | nan                           |
| O3 + MACR       | 0.9*MGLY + 0.45*HCOOH + 0.32*HO2 + 0.22*CO + 0.19*OH + 0.1*MeCO3                                                   | 7e-16    |    0    |       2100 | nan                           |
| OClO + NO       | NO2 + ClO                                                                                                          | 2.5e-12  |    0    |        600 | nan                           |
| OH + CH4        | H2O + MeOO                                                                                                         | 2.45e-12 |    0    |       1775 | nan                           |
| OH + CO         | H + CO2                                                                                                            | 1.44e-13 |    0    |          0 | pressure_dependent            |
| OH + ClO        | HCl + O2                                                                                                           | 6e-13    |    0    |       -230 | nan                           |
| OH + ClO        | HO2 + Cl                                                                                                           | 7.4e-12  |    0    |       -270 | nan                           |
| OH + ClONO2     | HOCl + NO3                                                                                                         | 1.2e-12  |    0    |        330 | nan                           |
| OH + H2         | H2O + H                                                                                                            | 2.8e-12  |    0    |       1800 | nan                           |
| OH + HBr        | H2O + Br                                                                                                           | 5.5e-12  |    0    |       -200 | nan                           |
| OH + HCHO       | H2O + HO2 + CO                                                                                                     | 5.4e-12  |    0    |       -135 | nan                           |
| OH + HCl        | H2O + Cl                                                                                                           | 1.8e-12  |    0    |        250 | nan                           |
| OH + HO2        | H2O + O2                                                                                                           | 4.8e-11  |    0    |       -250 | nan                           |
| OH + H2O2       | HO2 + H2O                                                                                                          | 2.9e-12  |    0    |        160 | nan                           |
| OH + HO2NO2     | H2O + NO2 + O2                                                                                                     | 3.2e-13  |    0    |       -690 | nan                           |
| OH + HOCl       | ClO + H2O                                                                                                          | 3e-12    |    0    |        500 | nan                           |
| OH + HONO2      | H2O + NO3                                                                                                          | 2.4e-14  |    0    |       -460 | water_dependent               |
| OH + MeOOH      | H2O + MeOO                                                                                                         | 1.89e-12 |    0    |       -190 | nan                           |
| OH + NO3        | HO2 + NO2                                                                                                          | 2.2e-11  |    0    |          0 | nan                           |
| OH + O3         | HO2 + O2                                                                                                           | 1.7e-12  |    0    |        940 | nan                           |
| OH + OClO       | HOCl + O2                                                                                                          | 1.4e-12  |    0    |       -600 | nan                           |
| OH + OH         | H2O + O(3P)                                                                                                        | 6.31e-14 |    2.6  |       -945 | nan                           |
| OH + C2H6       | H2O + EtOO                                                                                                         | 6.9e-12  |    0    |       1000 | nan                           |
| OH + C3H8       | i-PrOO + H2O                                                                                                       | 7.6e-12  |    0    |        585 | pressure_dependent            |
| OH + C3H8       | n-PrOO + H2O                                                                                                       | 7.6e-12  |    0    |        585 | pressure_dependent            |
| OH + C5H8       | ISO2                                                                                                               | 2.7e-11  |    0    |       -390 | nan                           |
| OH + EtCHO      | H2O + EtCO3                                                                                                        | 4.9e-12  |    0    |       -405 | nan                           |
| OH + EtOOH      | H2O + EtOO                                                                                                         | 1.9e-12  |    0    |       -190 | nan                           |
| OH + EtOOH      | H2O + MeCHO + OH                                                                                                   | 8.01e-12 |    0    |          0 | nan                           |
| OH + HACET      | MGLY + HO2                                                                                                         | 1.6e-12  |    0    |       -305 | nan                           |
| OH + HCOOH      | HO2                                                                                                                | 4.5e-13  |    0    |          0 | nan                           |
| OH + HONO       | H2O + NO2                                                                                                          | 2.5e-12  |    0    |       -260 | nan                           |
| OH + ISON       | HACET + NALD                                                                                                       | 1.3e-11  |    0    |          0 | nan                           |
| OH + ISOOH      | MACR + OH                                                                                                          | 1e-10    |    0    |          0 | nan                           |
| OH + MACR       | MACRO2                                                                                                             | 1.3e-12  |    0    |       -610 | nan                           |
| OH + MACR       | MACRO2                                                                                                             | 4e-12    |    0    |       -380 | nan                           |
| OH + MACROOH    | MACRO2                                                                                                             | 3.77e-11 |    0    |          0 | nan                           |
| OH + MGLY       | MeCO3 + CO                                                                                                         | 1.9e-12  |    0    |       -575 | nan                           |
| OH + MPAN       | HACET + NO2                                                                                                        | 2.9e-11  |    0    |          0 | nan                           |
| OH + Me2CO      | H2O + MeCOCH2OO                                                                                                    | 1.7e-14  |    0    |       -423 | nan                           |
| OH + Me2CO      | H2O + MeCOCH2OO                                                                                                    | 8.8e-12  |    0    |       1320 | nan                           |
| OH + MeCHO      | H2O + MeCO3                                                                                                        | 4.7e-12  |    0    |       -345 | nan                           |
| OH + MeCO2H     | MeOO                                                                                                               | 8e-13    |    0    |          0 | nan                           |
| OH + MeCO3H     | MeCO3                                                                                                              | 3.7e-12  |    0    |          0 | nan                           |
| OH + MeCOCH2OOH | H2O + MeCOCH2OO                                                                                                    | 1.9e-12  |    0    |       -190 | nan                           |
| OH + MeCOCH2OOH | OH + MGLY                                                                                                          | 8.39e-12 |    0    |          0 | nan                           |
| OH + MeOH       | HO2 + HCHO                                                                                                         | 2.85e-12 |    0    |        345 | nan                           |
| OH + MeONO2     | HCHO + NO2 + H2O                                                                                                   | 4e-13    |    0    |        845 | nan                           |
| OH + MeOOH      | H2O + HCHO + OH                                                                                                    | 2.12e-12 |    0    |       -190 | nan                           |
| OH + NALD       | HCHO + CO + NO2                                                                                                    | 4.7e-12  |    0    |       -345 | nan                           |
| OH + PAN        | HCHO + NO2 + H2O                                                                                                   | 3e-14    |    0    |          0 | nan                           |
| OH + PPAN       | MeCHO + NO2 + H2O                                                                                                  | 1.27e-12 |    0    |          0 | nan                           |
| OH + i-PrOOH    | Me2CO + OH                                                                                                         | 1.66e-11 |    0    |          0 | nan                           |
| OH + i-PrOOH    | i-PrOO + H2O                                                                                                       | 1.9e-12  |    0    |       -190 | nan                           |
| OH + n-PrOOH    | EtCHO + H2O + OH                                                                                                   | 1.1e-11  |    0    |          0 | nan                           |
| OH + n-PrOOH    | n-PrOO + H2O                                                                                                       | 1.9e-12  |    0    |       -190 | nan                           |
| DMS + OH        | SO2                                                                                                                | 1.2e-11  |    0    |        260 | nan                           |
| DMS + OH        | MSA + SO2                                                                                                          | 3.04e-12 |    0    |       -350 | nan                           |
| DMS + NO3       | SO2                                                                                                                | 1.9e-13  |    0    |       -500 | nan                           |
| DMS + O(3P)     | SO2                                                                                                                | 1.3e-11  |    0    |       -410 | nan                           |
| COS + O(3P)     | CO + SO2                                                                                                           | 2.1e-11  |    0    |       2200 | nan                           |
| COS + OH        | CO2 + SO2                                                                                                          | 1.1e-13  |    0    |       1200 | nan                           |
| SO2 + O3        | SO3                                                                                                                | 3e-12    |    0    |       7000 | nan                           |
| SO3 + H2O       | H2SO4 + H2O                                                                                                        | 8.5e-41  |    0    |      -6540 | nan                           |
| Monoterp + OH   | 0.13*Sec_Org                                                                                                       | 1.2e-11  |    0    |       -444 | nan                           |
| Monoterp + O3   | 0.13*Sec_Org                                                                                                       | 1.01e-15 |    0    |        732 | nan                           |
| Monoterp + NO3  | 0.13*Sec_Org                                                                                                       | 1.19e-12 |    0    |       -925 | nan                           |


## Table S2. Termolecular reactions

| reactants    | products     |   Fc |    k1_A |   k1_alpha |   k1_beta |    k2_A |   k2_alpha |   k2_beta |
|:-------------|:-------------|-----:|--------:|-----------:|----------:|--------:|-----------:|----------:|
| O(3P) + O2   | O3           | 0    | 6e-34   |       -2.5 |         0 | 0       |        0   |         0 |
| O(3P) + NO   | NO2          | 0.6  | 9e-32   |       -1.5 |         0 | 3e-11   |        0   |         0 |
| O(3P) + NO2  | NO3          | 0.6  | 2.5e-31 |       -1.8 |         0 | 2.2e-11 |       -0.7 |         0 |
| O(1D) + N2   | N2O          | 0    | 2.8e-36 |       -0.9 |         0 | 0       |        0   |         0 |
| BrO + NO2    | BrONO2       | 0.6  | 5.2e-31 |       -3.2 |         0 | 6.9e-12 |        0   |         0 |
| ClO + ClO    | Cl2O2        | 0.6  | 1.6e-32 |       -4.5 |         0 | 3e-12   |       -2   |         0 |
| Cl2O2        | ClO + ClO    | 0.45 | 3.7e-07 |        0   |      7690 | 1.8e+14 |        0   |      7690 |
| ClO + NO2    | ClONO2       | 0.6  | 1.8e-31 |       -3.4 |         0 | 1.5e-11 |        0   |         0 |
| H + O2       | HO2          | 0.6  | 4.4e-32 |       -1.3 |         0 | 7.5e-11 |        0   |         0 |
| HO2 + HO2    | H2O2 + O2    | 0    | 2.1e-33 |        0   |      -920 | 0       |        0   |         0 |
| HO2 + NO2    | HO2NO2       | 0.6  | 2e-31   |       -3.4 |         0 | 2.9e-12 |        0   |         0 |
| HO2NO2       | HO2 + NO2    | 0.5  | 4.1e-05 |        0   |     10650 | 4.8e+15 |        0   |     11170 |
| OH + NO      | HONO         | 0.6  | 7e-31   |       -2.6 |         0 | 3.6e-11 |       -0.1 |         0 |
| OH + NO2     | HONO2        | 0.6  | 1.8e-30 |       -3   |         0 | 2.8e-11 |        0   |         0 |
| OH + OH      | H2O2         | 0.6  | 6.9e-31 |       -1   |         0 | 2.6e-11 |        0   |         0 |
| MeCO3 + NO2  | PAN          | 0.3  | 2.7e-28 |       -7.1 |         0 | 1.2e-11 |       -0.9 |         0 |
| PAN          | MeCO3 + NO2  | 0.3  | 0.0049  |        0   |     12100 | 5.4e+16 |        0   |     13830 |
| EtCO3 + NO2  | PPAN         | 0.3  | 2.7e-28 |       -7.1 |         0 | 1.2e-11 |       -0.9 |         0 |
| PPAN         | EtCO3 + NO2  | 0.3  | 0.0049  |        0   |     12100 | 5.4e+16 |        0   |     13830 |
| MACRO2 + NO2 | MPAN         | 0.3  | 2.7e-28 |       -7.1 |         0 | 1.2e-11 |       -0.9 |         0 |
| MPAN         | MACRO2 + NO2 | 0.3  | 0.0049  |        0   |     12100 | 5.4e+16 |        0   |     13830 |
| NO2 + NO3    | N2O5         | 0.35 | 3.6e-30 |       -4.1 |         0 | 1.9e-12 |        0.2 |         0 |
| N2O5 + M     | NO2 + NO3    | 0.35 | 0.0013  |       -3.5 |     11000 | 9.7e+14 |        0.1 |     11080 |
| NO + NO      | NO2 + NO2    | 0    | 3.3e-39 |        0   |      -530 | 0       |        0   |         0 |
| SO2 + OH     | SO3 + HO2    | 0.6  | 3e-31   |       -3.3 |         0 | 1.5e-12 |        0   |         0 |


## Table S3. Photodissociation reactions

| reactants       | products                 |
|:----------------|:-------------------------|
| BrCl + hv       | Br + Cl                  |
| BrO + hv        | Br + O(3P)               |
| BrONO2 + hv     | Br + NO3                 |
| BrONO2 + hv     | BrO + NO2                |
| CF2Cl2 + hv     | Cl + Cl                  |
| CFCl3 + hv      | Cl + Cl + Cl             |
| CH4 + hv        | MeOO + H                 |
| Cl2O2 + hv      | Cl + Cl + O2             |
| ClONO2 + hv     | Cl + NO3                 |
| ClONO2 + hv     | ClO + NO2                |
| CO2 + hv        | CO + O(3P)               |
| COS + hv        | CO + SO2                 |
| EtCHO + hv      | EtOO + HO2 + CO          |
| EtOOH + hv      | MeCHO + HO2 + OH         |
| H2O + hv        | OH + H                   |
| H2O2 + hv       | OH + OH                  |
| H2SO4 + hv      | SO3 + OH                 |
| HACET + hv      | MeCO3 + HCHO + HO2       |
| HCHO + hv       | HO2 + HO2 + CO           |
| HCHO + hv       | H2 + CO                  |
| HCl + hv        | H + Cl                   |
| HO2NO2 + hv     | HO2 + NO2                |
| HO2NO2 + hv     | OH + NO3                 |
| HOBr + hv       | OH + Br                  |
| HOCl + hv       | OH + Cl                  |
| HONO + hv       | OH + NO                  |
| HONO2 + hv      | OH + NO2                 |
| i-PrOOH + hv    | Me2CO + HO2 + OH         |
| ISON + hv       | NO2 + MACR + HCHO + HO2  |
| ISOOH + hv      | OH + MACR + HCHO + HO2   |
| MACR + hv       | MeCO3 + HCHO + CO + HO2  |
| MACROOH + hv    | OH + HO2 + OH + HO2      |
| MACROOH + hv    | HACET + CO + MGLY + HCHO |
| Me2CO + hv      | MeCO3 + MeOO             |
| MeBr + hv       | Br + H                   |
| MeCHO + hv      | MeOO + HO2 + CO          |
| MeCHO + hv      | CH4 + CO                 |
| MeCO3H + hv     | MeOO + OH                |
| MeCOCH2OOH + hv | MeCO3 + HCHO + OH        |
| MeONO2 + hv     | HO2 + HCHO + NO2         |
| MeOOH + hv      | HO2 + HCHO + OH          |
| MGLY + hv       | MeCO3 + CO + HO2         |
| MPAN + hv       | MACRO2 + NO2             |
| N2O + hv        | N2 + O(1D)               |
| N2O5 + hv       | NO2 + NO3                |
| NALD + hv       | HCHO + CO + NO2 + HO2    |
| NO + hv         | N + O(3P)                |
| NO2 + hv        | NO + O(3P)               |
| NO3 + hv        | NO + O2                  |
| NO3 + hv        | NO2 + O(3P)              |
| n-PrOOH + hv    | EtCHO + HO2 + OH         |
| O2 + hv         | O(3P) + O(3P)            |
| O2 + hv         | O(3P) + O(1D)            |
| O3 + hv         | O2 + O(1D)               |
| O3 + hv         | O2 + O(3P)               |
| OClO + hv       | O(3P) + ClO              |
| PAN + hv        | MeCO3 + NO2              |
| PPAN + hv       | EtCO3 + NO2              |
| SO3 + hv        | SO2 + O(3P)              |


## Table S4. Heterogeneous reactions

| reactants    | products         | gamma_liquid_aerosol   |   gamma_NAT |   gamma_ice |
|:-------------|:-----------------|:-----------------------|------------:|------------:|
| ClONO2 + HCl | Cl + Cl + HONO2  | f                      |      0.3    |        0.3  |
| ClONO2 + H2O | HOCl + HONO2     | 0.006                  |    nan      |        0.3  |
| N2O5 + H2O   | HONO2 + HONO2    | 0.1                    |      0.0006 |        0.03 |
| N2O5 + HCl   | Cl + NO2 + HONO2 | nan                    |      0.003  |        0.03 |
| HOCl + HCl   | Cl + Cl + H2O    | f                      |    nan      |        0.3  |


## Table S5. Aqueous-phase sulfur cycle reactions

| reactants            | products    | rate_expression_cm3_molecule-1_s-1                 | notes                                |
|:---------------------|:------------|:---------------------------------------------------|:-------------------------------------|
| HSO3-(aq) + H2O2(aq) | SO4(2-)(aq) | 2.1295E+14*exp(-4430.0/T)*([H+]/(1.0 + 13.0*[H+])) | H+ prescribed at 1E-5 molecules cm-3 |
| HSO3-(aq) + O3(aq)   | SO4(2-)(aq) | 4.0113E+13*exp(-5530.0/T)                          | nan                                  |
| SO3(2-)(aq) + O3(aq) | SO4(2-)(aq) | 7.43E+16*exp(-5280.0/T)                            | nan                                  |


## Table S6. Henry's law data: soluble tropospheric species

| species    |   KH_298K_M_atm-1 |   neg_dH_R_K |   Ka_298K_M |   neg_dH_R_dissoc_K |
|:-----------|------------------:|-------------:|------------:|--------------------:|
| NO3        |           2       |         2000 |     0       |                   0 |
| N2O5       |      210000       |         8700 |    20       |                   0 |
| HO2NO2     |       13000       |         6900 |     1e-05   |                   0 |
| HONO2      |      210000       |         8700 |    20       |                   0 |
| HO2        |        4000       |         5900 |     2e-05   |                   0 |
| H2O2       |       83000       |         7400 |     2.4e-12 |               -3730 |
| HCHO       |        3300       |         6500 |     0       |                   0 |
| MeOO       |        2000       |         6600 |     0       |                   0 |
| MeOOH      |         310       |         5000 |     0       |                   0 |
| HONO       |          50       |         4900 |     0.00056 |               -1260 |
| EtOOH      |         340       |         5700 |     0       |                   0 |
| n-PrOOH    |         340       |         5700 |     0       |                   0 |
| i-PrOOH    |         340       |         5700 |     0       |                   0 |
| MeCOCH2OOH |         340       |         5700 |     0       |                   0 |
| ISOOH      |           1.7e+06 |         9700 |     0       |                   0 |
| ISON       |        3000       |         7400 |     0       |                   0 |
| MACROOH    |           1.7e+06 |         9700 |     0       |                   0 |
| HACET      |         140       |         7200 |     0       |                   0 |
| MGLY       |        3500       |         7200 |     0       |                   0 |
| HCOOH      |        6900       |         5600 |     0.00018 |               -1510 |
| MeCO3H     |         750       |         5300 |     6.3e-09 |                   0 |
| MeCO2H     |        4700       |         6000 |     1.8e-05 |                   0 |
| MeOH       |         230       |         4900 |     0       |                   0 |


## Table S7. Henry's law data: soluble stratospheric species

| species   |   KH_298K_M_atm-1 |   neg_dH_R_K |   Ka_298K_M |   neg_dH_R_dissoc_K |
|:----------|------------------:|-------------:|------------:|--------------------:|
| BrONO2    |          210000   |         8700 |   157       |                   0 |
| HCl       |              19   |          600 | 10000       |                   0 |
| HOCl      |             920   |         5900 |     3.2e+06 |                   0 |
| HBr       |               1.3 |        10200 |     1e+09   |                   0 |
| HOBr      |           61000   |            0 |     0       |                   0 |
| ClONO2    |          210000   |         8700 |    15.7     |                   0 |


## Table S8. Henry's law data: aerosol precursor species

| species   |   KH_298K_M_atm-1 |   neg_dH_R_K |   Ka_298K_M |   neg_dH_R_dissoc_K |
|:----------|------------------:|-------------:|------------:|--------------------:|
| O3        |            0.0113 |         2300 |      0      |                   0 |
| SO2       |            1.23   |         3020 |      0.0123 |                2010 |
| DMSO      |        50000      |         6425 |      0      |                   0 |

