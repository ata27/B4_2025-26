# B4 — Chemistry in the Atmosphere (Part II)

Modular lecture notes and companion Python notebooks for the Cambridge Chemistry
Part II course B4, *Chemistry in the Atmosphere*. Built from the Michaelmas
(Lectures 1–6) and Lent (Lectures 7–12) course notes.

## Structure

```
lectures/     Modular markdown lecture notes, one file per topic
notebooks/    Companion Jupyter notebooks (paired 1:1 with lectures where noted)
assets/       Figures used in the lecture notes
data/         Reference datasets used by the notebooks (see data/README.md)
scripts/      Scripts used to generate reference data, for reproducibility
```

## Modules

**Michaelmas term (Lectures 1–6)**

| # | Lecture(s) | Title |
|---|---|---|
| 1 | 1 | Basic Physical and Chemical Structure of the Troposphere and Stratosphere |
| 2 | 2 | Chemical Kinetics in the Atmosphere |
| 3 | 3 | Atmospheric Photochemistry |
| 4 | 4–5 | Stratospheric Ozone Chemistry: the Chapman Mechanism and Catalytic Cycles |
| 5 | 6 | Model Predictions of Changes in Global O₃ |
| 5b | Bonus | Measurement Techniques for Stratospheric Composition |

**Lent term (Lectures 7–12)**

| # | Lecture(s) | Title |
|---|---|---|
| 6 | 7 | Atmospheric Composition: Sources, Sinks and Lifetimes |
| 7 | 8 | Tropospheric Photochemistry and the Hydroxyl Radical |
| 8 | 9 | Methane Oxidation and NOx-Driven Ozone Production |
| 9 | 10 | The Tropospheric Ozone Budget, Carbonyl Formation and NOx Reservoirs |
| 10 | 11 | Oxidation of Non-Methane Organic Compounds I: Alkanes and Alkenes |
| 11 | 12 | Oxidation of Non-Methane Organic Compounds II: Aromatics and Oxygenated Organics |

Every module has a paired, pre-executed Jupyter notebook in `notebooks/`, cross-linked from the
bottom of each lecture file. Start at `lectures/01-basic-structure-troposphere-stratosphere.md`
and follow the "Next" links, or jump straight to whichever lecture you need.

## Using the notebooks

Each notebook only needs `numpy`, `scipy`, and `matplotlib`. To run locally:

```bash
pip install numpy scipy matplotlib jupyter
jupyter notebook notebooks/
```

Or open directly in **Google Colab** / **Binder** via the badge links once the repo is public (add after first push — see below).

## Attribution

Notes originally authored by Prof. Alexander T. Archibald (and, per the original
course materials, based in part on an earlier course taught by Prof. John Pyle).
