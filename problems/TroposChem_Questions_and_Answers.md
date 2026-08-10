# Exercises — Part II Chemistry in the Atmosphere: Tropospheric Chemistry (Lent 2024)

*Worked solutions and supervisor notes are hidden by default — click "Show answer" or "Supervisor notes" under each question to reveal them.*

*Students will also find past tripos questions since 2015 relevant to the content of this course.*

## Chapter 1

**1.** The deposition velocity of ozone to the ground is 10⁻² m s⁻¹ and the mixed layer height is 500 m.

(a) If the rate of photochemical ozone production is approximately constant at 10 ppb/hr during the day, what is the maximum possible [O₃]?

<details>
<summary><b>Show answer</b></summary>

[O₃] = Rp/L¹

In this case we need to convert the rate of production or first order loss so that we have something with the same units. I prefer to convert 10 ppb/hr into 6.9×10⁷ molecules cm⁻³ s⁻¹.

L¹ = v_d/Z_bl = 1 cm s⁻¹ / 50000 cm (i.e. deposition over a well-mixed boundary layer of 500 m)

This leads to an **[O₃] = 3.45×10¹² cm⁻³ (or 138 ppb)**.

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*This is the main question focusing on deposition so please make sure the students are comfortable with the concept. The key points as I see it are to get them to think about the vertical length scale over which the species concentration is uniform, as this determines the length scale over which deposition acts.*

</details>

(b) Is this concentration likely to be achieved?

<details>
<summary><b>Show answer</b></summary>

No. This is a very high mixing ratio.

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*Make sure to discuss why! I would suggest that the students be encouraged to think about the timescales for other processes. For example, mixing! They should have a feel for vertical and horizontal mixing times. A nice way to visualize this is also to look at the air quality forecasts on windy.com where you can see NO₂, aerosols etc and the wind vectors.*

</details>

**2.** Methyl Chloroform (1,1,1-trichlorethane) is an Ozone Depleting Substance formerly used widely as a solvent. Under the provisions of the Montreal Protocol its production and release ceased in 1992. The observed mean concentrations of Methyl Chloroform in the troposphere in recent years are given below:

| Year | 1993 | 1994 | 1995 | 1996 | 1997 | 1998 | 1999 |
|---|---|---|---|---|---|---|---|
| [CCl₃CH₃] / pptv | 152 | 129 | 112 | 99 | 82 | 70 | 61 |

(a) Use this data to determine the atmospheric lifetime of Methyl Chloroform. The release rate prior to the control was 1.2 × 10¹² g yr⁻¹.

<details>
<summary><b>Show answer</b></summary>

Note, MCF = methyl chloroform (CCl₃CH₃).

Students should plot a ln[MCF] vs time graph. This gives a nice straight line with gradient −0.15 (i.e. 0.15 years⁻¹). **τ = 1/0.15 = 6.6 years.**

</details>

(b) What would the steady-state volume mixing ratio of Methyl Chloroform have been if emissions had continued at this rate? Assume a uniformly mixed atmosphere.

<details>
<summary><b>Show answer</b></summary>

At steady state:

[MCF] = Rate of production / first order loss

We will assume that there is no impact on the first order loss of MCF through its abundance (probably a very good assumption) so we will keep that constant at 0.15 years⁻¹.

Rate of production is then the emissions / the mass of the atmosphere. We calculated this in Question 1 of the first set of problems to be ~5.15×10¹⁸ kg.

This will give us a mass mixing ratio (2.3×10⁻¹⁰ kg MCF year⁻¹ kg⁻¹ air). To then get a molar mixing ratio (assuming ideal gas behaviour) we need to convert through the ratio of the molar masses (i.e. multiply the mass mixing ratio by 28.8/133.5). This results in a rate of production of:

Rp = 49.6 ppt year⁻¹

**[MCF] = 49.6 ppt year⁻¹ / 0.15 year⁻¹ = 330 ppt**

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*Depending on how the students make assumptions about mixing over the whole atmosphere vs troposphere, they may modify the mass they dilute the emissions over, so I would award marks for calculations that are sensible.*

</details>

**3.** Methyl Chloroform is removed from the atmosphere by reaction with OH radicals:

OH + CCl₃CH₃ → H₂O + CCl₃CH₂

Estimate the global mean concentration of OH using the results from the analysis above (k = 1.2 × 10⁻¹⁴ cm³ molecule⁻¹ s⁻¹) and comment on your result.

<details>
<summary><b>Show answer</b></summary>

[OH] = 0.15 / k′, where k′ = k × 3.17×10⁷ (a conversion factor to go from seconds to years).

**[OH] = 3.96×10⁵ cm⁻³.**

This is reasonably in line with what's been said in the lectures — [OH] ~ 10⁶ cm⁻³ — but is a bit lower. Why could this be?

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*Get the students to discuss why this could be. How would extra sinks of MCF affect the calculation? What about extra sources? What about the temperature dependence of the rate constant? If it was temperature dependent, how would that affect things?*

</details>

## Chapter 2

**1.** At wavelengths below 398 nm the quantum yield for the photolysis of NO₂ is unity:

- NO₂ + hν → O + NO, J_NO2
- O + O₂ + M → O₃ + M
- NO + O₃ → NO₂ + O₂

The average values for the NO₂ absorption cross section (cm² molecule⁻¹) and the daytime solar flux (photons cm⁻² s⁻¹) in the 300–398 nm region at the earth's surface are 3.0 × 10⁻¹⁹ and 2.75 × 10¹⁶ respectively.

(a) What is the value of the photolysis constant for NO₂, J_NO2?

<details>
<summary><b>Show answer</b></summary>

**JNO₂ = 8.25×10⁻³ s⁻¹**

</details>

(b) Assume photostationary state for O₃, NO and NO₂, i.e., for the three reactions outlined above. If [O₃] = 60 ppbv and [NOx] = 15 ppbv, what is the concentration of NO₂ in the sunlit atmosphere? (Rate constant for NO + O₃ reaction = 2.0 × 10⁻¹⁴ cm³ molecule⁻¹ s⁻¹, 1 bar = 2.46 × 10¹⁹ molecule cm⁻³.)

<details>
<summary><b>Show answer</b></summary>

[NO₂] = k3[NO][O₃] / J1

As [NOx] = [NO] + [NO₂] then [NO] = [NOx] − [NO₂] (substitute this into the expression above):

**[NO₂] = k3[NOx][O₃] / (J1 + k3[O₃]) = 11.7 ppb = 2.88×10¹¹ cm⁻³**

An aside:

[NO]/[NO₂] = J1/(k3[O₃]) = 0.279, hence [NO₂]/[NO] = 3.578, or [NO₂] = 3.578×[NO].

</details>

**2.** Photolysis of O₃ in the troposphere leads to the production of hydroxyl radicals.

(a) Outline the sequence of reactions that lead to OH formation and derive an expression for the rate of OH formation in terms of the photolysis rate of ozone at wavelengths less than approximately 310 nm (J₂), the concentrations of O₃, H₂O and the total gas concentration, M.

<details>
<summary><b>Show answer</b></summary>

O₃ + hν → O(¹D) + O₂, J1

O(¹D) + H₂O → OH + OH, k2

O(¹D) + M → O(³P) + M, k3

d[OH]/dt = 2×k2[O1D][H2O]

Put [O1D] into steady state:

[O1D] = J1[O3] / (k2[H2O] + k3[M])

So, **d[OH]/dt = 2×k2[H2O] × J1[O3] / (k2[H2O] + k3[M])**  (A)

</details>

(b) What is the mean rate of production of OH from this process for the surface atmospheric conditions (1 bar and 298 K) where the relative humidity is 50% and the local ozone concentration is 1 × 10¹² molecules cm⁻³?

J(O¹D) = 3 × 10⁻⁵ s⁻¹, k(O(¹D) + H₂O)/k(O¹D + air) = 7.1, saturated vapour pressure of water is 30 mbar at 298 K.

<details>
<summary><b>Show answer</b></summary>

At 50% RH the [H2O] = 0.5×30 mbar = 15×10⁻³ bar = 3.75×10¹⁷ cm⁻³

In my nomenclature, k2/k3 = 7.1.

Re-write (A):

d[OH]/dt = 2×7.1[H2O] × J1[O3] / (k2[H2O] + [M])

Now, multiply by k3 and re-arrange:

d[OH]/dt = 2×7.1[H2O] × J1[O3] / (7.1×[H2O] + [M]) = **5.77×10⁶ cm⁻³ s⁻¹**

</details>

(c) How do you expect OH production to vary with altitude in the troposphere?

![OH production rate vs. altitude and latitude](media/chapter2_OH_altitude_profile.png)

<details>
<summary><i>Supervisor notes</i></summary>

*Not looking for an essay here, but an argument based on the basic points that [H2O] is very important for the production of OH. As it decreases as we go higher in the troposphere, then d[OH]/dt should decrease. This is in spite of increases in O₃ and J.*

</details>

(d) In clean air at the earth's surface (pressure = 1 bar, temperature 298 K), OH is removed primarily by its reaction with CO:

OH + CO → H + CO₂, k_CO = 2 × 10⁻¹³ cm³ s⁻¹

Write an expression for the steady state concentration of OH and evaluate it using the following information:

J₂ = 2.7 × 10⁻⁵ s⁻¹; [O₃] = 40 ppbv; [CO] = 100 ppbv; [H₂O] = 0.02 bar

k(O(¹D) + M) = 3 × 10⁻¹¹ cm³ s⁻¹, k(O(¹D) + H₂O) = 2.2 × 10⁻¹⁰ cm³ s⁻¹

<details>
<summary><b>Show answer</b></summary>

d[OH]/dt = 2×k2[O1D][H2O] − k_CO[OH][CO]

[OH] = Rate of production / first order loss = Rp/(k_CO[CO])

**[OH] = 1.38×10⁷ cm⁻³**

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*I would suggest discussing this answer as it's quite different to the answer to Chapter 1 Q3. I think the main issue here is (1) the use of a single sink for OH, (2) a high [H2O] mixing ratio (2%). This is similar to the tropics!*

</details>

**3.** The following simplified reaction scheme provides a description of the chemistry governing concentrations of OH and HO₂ in the troposphere:

| Reaction | Rate coefficient (cm³ s⁻¹ unless noted) |
|---|---|
| O₃ + hν (λ<315 nm) → O(¹D) + O₂ | k₁ = 2.5 × 10⁻⁶ s⁻¹ |
| O(¹D) + M → O(³P) + M | k₂ = 3.0 × 10⁻¹¹ |
| O(¹D) + H₂O → 2OH | k₃ = 2.2 × 10⁻¹⁰ |
| CO + OH → CO₂ + H | k₄ = 2.1 × 10⁻¹³ |
| H + O₂ + M → HO₂ + M | k₅ (very fast) |
| HO₂ + O₃ → OH + 2O₂ | k₆ = 2.0 × 10⁻¹⁵ |
| HO₂ + HO₂ → H₂O₂ + O₂ | k₇ = 3.5 × 10⁻¹² |

Temperature = 298 K; pressure = 1 bar ([M] = 2.46 × 10¹⁹ cm⁻³).

(a) Derive an expression for the steady state concentration of HOx radicals (OH + HO₂).

<details>
<summary><b>Show answer</b></summary>

**d[HOx]/dt = 2×k3[O1D][H2O] − 2×k7[HO₂]² = 0**

</details>

(b) Evaluate [OH] in the lower troposphere for [CO] = 100 ppbv; [O₃] = 40 ppbv; and [H₂O] = 0.02 bar. You may assume that HOx interconversion by reactions 4 and 6 is rapid.

<details>
<summary><b>Show answer</b></summary>

[HO₂] = √( k3[O1D][H2O] / k7 )

[OH]/[HO2] = k6[O3] / (k4[CO])

Putting in the numbers:

[O1D] = 2.9×10⁻³ cm⁻³

[HO₂] = 3×10⁸ cm⁻³

**[OH] = 1.14×10⁶ cm⁻³**

However, if you actually solve this system numerically you get [OH] = 2.3×10⁶ cm⁻³. This is what you would get if you calculated OH as:

OH = (2×k3×O1D×H2O + k6×HO2×O3) / (k4×CO)

This is because the rate of production of OH via O1D+H2O is actually faster than the interconversion of HO2-to-OH. But you cannot solve part (e) unless you assume HOx interconversion is rapid, i.e. [OH]/[HO2] = k6[O3] / (k4[CO]).

Again, numerical solutions to the HO2/OH ratio come out at about 128, whereas the "clue" in the question gives you about 260.

</details>

(c) How would the steady state of HOx radicals vary with solar intensity?

<details>
<summary><b>Show answer</b></summary>

As the expression above shows, it would vary with the square root of solar intensity.

</details>

(d) What is the effect of these processes on tropospheric ozone?

<details>
<summary><b>Show answer</b></summary>

As the reactions show, in the absence of NOx, this scheme leads to net O3 destruction — mainly through the reaction of O1D to form HOx and the reaction of HOx with O3.

</details>

In the presence of NOx (NO + NO₂), the following reactions occur:

| Reaction | Rate coefficient (cm³ s⁻¹) |
|---|---|
| HO₂ + NO → OH + NO₂ | k₈ = 8.6 × 10⁻¹² |
| NO₂ + OH → HNO₃ | k₉ = 1.1 × 10⁻¹¹ |

(e) Assuming NO = 0.1 ppb and NO2 = 0.36 ppb, derive a new expression for the HOx steady state.

<details>
<summary><b>Show answer</b></summary>

Now we have an extra HOx sink (reaction 9) and an extra interconversion reaction (reaction 8):

d[HOx]/dt = 2×k3[O1D][H2O] − 2×k7[HO₂]² − k9[NO2][OH] = 0  (A)

[OH]/[HO2] = (k6[O3] + k8[NO]) / (k4[CO])  (B)

We can calculate [OH] = [HO2]×(B) and substitute that into (A):

d[HOx]/dt = 2×k3[O1D][H2O] − 2×k7[HO₂]² − k9[NO2][HO2]×(B) = 0  (C)

Which looks like a quadratic equation (x = [HO₂]) which we can solve, noting that here (c) = the rate of production of HOx, (b) = k9[NO2], and (a) = 2×k7.

Plugging in numbers: (c) = 2.9×10⁻³ × 0.02 × 2.46×10¹⁹ × 2 × 2.2×10⁻¹⁰ = 6.28×10⁵ cm⁻³ s⁻¹

(a) = 7×10⁻¹² cm³ s⁻¹, and (b) = 1.1×10⁻¹¹ × 0.36×10⁻⁹ × 2.46×10¹⁹ × ((2×10⁻¹⁵×40×10⁻⁹×2.46×10¹⁹) + (8.6×10⁻¹²×0.1×10⁻⁹×2.46×10¹⁹)) / (2.1×10⁻¹³×100×10⁻⁹×2.46×10¹⁹) = **4.36×10⁻³**

**[HO2] = 1.2×10⁸ cm⁻³**

</details>

(f) Evaluate [OH].

<details>
<summary><b>Show answer</b></summary>

Now the [OH] will have changed because of k8: **new [OH] = 4.9×10⁶ cm⁻³**.

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*If the students got the sign of the change wrong then get them to think about this qualitatively. What would you expect upon adding in reactions 8 and 9? Overall, reaction 9 means HOx should go down and adding in reaction 8 means the HO2:OH ratio should go down.*

</details>

(g) Comment on its dependence on solar intensity.

<details>
<summary><b>Show answer</b></summary>

Basically now there is less dependence, as can be seen from the quadratic equation.

</details>

## Chapter 3

**1.** The dominant loss process for tropospheric CH₄ is by the reaction:

OH + CH₄ → CH₃ + H₂O, k₁ = 7.7 × 10⁻¹⁵ cm³ molecule⁻¹ s⁻¹

The production rate of OH from the O(¹D) + H₂O reaction P = 5 × 10⁵ molecule cm⁻³ s⁻¹ and OH is lost only by reaction with CH₄ and with CO.

OH + CO → H + CO₂, k₂ = 2.0 × 10⁻¹³ cm³ molecule⁻¹ s⁻¹

(a) Evaluate the steady state concentration of OH ([CO] = 100 ppb and [CH₄] = 1.7 ppm).

<details>
<summary><b>Show answer</b></summary>

At steady state:

[OH] = Rp/L1 = 5×10⁵ cm⁻³ s⁻¹ / (k1[CH4] + k2[CO])

**[OH] = 6.1×10⁵ cm⁻³**

</details>

(b) Estimate the mean chemical lifetime of CH₄ in the troposphere.

<details>
<summary><b>Show answer</b></summary>

**τ = 1/(k1[OH]) = 6.75 years**

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*Make sure they convert to years, not a huge number of seconds.*

</details>

(c) What vertical profile would you expect for CH₄ in the troposphere?

<details>
<summary><b>Show answer</b></summary>

Would expect a constant mixing ratio. This lifetime is much longer than the time scale for mixing across the hemisphere and troposphere, so would also expect a tropospheric uniform value. In reality this is not quite seen and there is a latitudinal gradient. This is largely a function of the [OH] not being uniform, so that the value of tau they calculated is an "average".

</details>

**2.** The ratio of OH to HO₂ in the lower atmosphere is governed mainly by the following reactions:

- OH + CO → CO₂ + H, k₁ = 2 × 10⁻¹³ cm³ molec.⁻¹ s⁻¹
- H + O₂ + M → HO₂ + M (very fast)
- HO₂ + NO → NO₂ + OH, k₂ = 8 × 10⁻¹² cm³ molec.⁻¹ s⁻¹

(a) Evaluate the steady state concentration of HO₂ for the following trace gas concentrations (in molec. cm⁻³): [OH] = 4 × 10⁶, [NO] = 1.2 × 10⁹, [CO] = 4 × 10¹², [O₃] = 40 ppb (p=1 atm, T = 298 K).

<details>
<summary><b>Show answer</b></summary>

**[HO₂] = k1[CO][OH] / (k2[NO]) = 3.3×10⁸ cm⁻³**

</details>

The steady state of NO is controlled by reaction (2) plus the following reactions:

- NO₂ + hν → NO + O, J₃ = 1 × 10⁻² s⁻¹
- O + O₂ + M → O₃ + M (very fast)
- O₃ + NO → NO₂ + O₂, k₄ = 2 × 10⁻¹⁴ cm³ molec.⁻¹ s⁻¹

(b) Derive an expression for the rate of ozone production and evaluate it for the above concentrations. You may assume that the ratio [NO₂]/[NO] is approximated by the photostationary state, i.e. reactions 2, 3 and 4.

<details>
<summary><b>Show answer</b></summary>

d[O3]/dt = J3[NO2] − k4[NO][O3]

From the NOx steady state we have:

[NO]/[NO₂] = J3 / (k2[HO₂] + k4[O₃])

Or [NO2] = [NO]×(k2[HO₂] + k4[O₃]) / J3

We now get:

d[O3]/dt = k2[HO2][NO]

**d[O₃]/dt = 3.2×10⁶ molecules cm⁻³ s⁻¹ = 0.46 ppb/hr**

</details>

**3.** Peroxy acetyl nitrate (PAN) is a characteristic product of atmospheric photochemical degradation of non-methane hydrocarbons. It is formed by the addition reaction of acetyl peroxy radicals with NO₂. It reacts only very slowly with OH radicals, is not photolysed but thermally decomposes by the following mechanism:

CH₃C(O)O₂NO₂ ⇌ CH₃C(O)O₂ + NO₂, k₁/k₋₁

CH₃C(O)O₂ + NO → CH₃ + CO₂ + NO₂, k₂

followed by oxidation of CH₃ to formaldehyde.

(a) Derive an expression for the overall rate of thermal decomposition of PAN in an atmosphere containing NO and NO₂ and also an expression for its lifetime.

<details>
<summary><b>Show answer</b></summary>

Let's call CH₃C(O)O₂NO₂ — PAN and CH₃C(O)O₂ — PA.

d[PAN]/dt = k₋₁[PA][NO2] − k1[PAN]

Put [PA] into steady state:

[PA] = k1[PAN] / (k₋₁[NO2] + k2[NO])

Substitute into the first expression:

d[PAN]/dt = k₋₁{k1[PAN]/(k₋₁[NO2] + k2[NO])}[NO2] − k1[PAN]

Rearranging (note the change in sign), the term k1{…} can be thought of as a first order rate of loss of PAN. The lifetime is then just the reciprocal of this expression.

</details>

(b) In daylight, the ratio [NO₂]/[NO] is governed primarily by the photostationary state involving the following reactions:

- NO₂ + hν → NO + O, J4
- O + O₂ + M → O₃ + M, k3 (v. fast)
- NO + O₃ → NO₂ + O₂, k5

Derive an expression for the ratio [NO₂]/[NO].

<details>
<summary><b>Show answer</b></summary>

[NO]/[NO₂] = J4/(k5[O3])

So **[NO₂]/[NO] = k5[O3]/J4**

NB this will be sensitive to the [M] assumed (or calculated).

</details>

(c) Evaluate the lifetime of PAN at 298 K in sunlit boundary layer, with [O₃] = 50 ppb and J4 = 1 × 10⁻² s⁻¹.

<details>
<summary><b>Show answer</b></summary>

At 298 K, working through the ratio [NO]/[NO₂] and the resulting first-order loss rate for PAN:

[NO]/[NO₂] = 0.446

1 + (k2/k₋₁)[NO]/[NO2] = 1 + 2(0.446) = 1.892

1 − 1/1.892 = 0.471

lifetime = 1/(0.471 k1) = 4684 s = **1.3 hours**

</details>

(d) A parcel of polluted boundary layer air containing PAN is transferred by convection to 5 km altitude where the ambient daytime temperature is 260 K. Assuming that J4 and the mixing ratio of O3 are independent of altitude, calculate the chemical lifetime of PAN at 5 km.

Data: k1 = 4.0 × 10¹⁵ exp(−13000/T) s⁻¹; k₋₁/k2 = 0.5 (independent of temperature); k5 = 2.0 × 10⁻¹² exp(−1400/T) cm³ molecule⁻¹ s⁻¹; 1 ppb = 2.46 × 10¹⁰ molecule cm⁻³ at 298 K and 1 bar; atmospheric pressure at 5 km = 0.542 bar.

<details>
<summary><b>Show answer</b></summary>

At T = 260 K:

k1 = 4×10¹⁵ exp(−13000/260) = 7.7×10⁻⁷ s⁻¹

k5 = 2×10⁻¹² exp(−1400/260) = 9.2×10⁻¹⁵ cm³ s⁻¹

[O3] = 6.67×10¹¹ molecules cm⁻³

[NO]/[NO2] = 1.63

1 + (k2/k₋₁)[NO]/[NO2] = 4.26

1 − 1/4.26 = 0.765

lifetime = 1/(0.765 k1) = 1.7×10⁶ s ≈ **19.6 days (~20 days)**

</details>

## Chapter 4

**1.** Outline, in brief, the role that organic peroxy radicals play in the formation of tropospheric ozone.

<details>
<summary><b>Show answer</b></summary>

Organic peroxy radicals (RO₂) propagate the conversion of NO-NO₂ without consuming O₃. In this way they are key intermediates for the production of tropospheric ozone (which is formed from the photolysis of NO₂).

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*This is the key point. Make sure the students are confident with this. The chemistry gets quite complex and confusing but they should be able to think about RO₂ as being a class of species with a simple and important role in perturbing the NOx photostationary state.*

</details>

**2.** What is the main difference in the oxidation schemes of alkanes and alkenes?

<details>
<summary><b>Show answer</b></summary>

The main things to focus on are:

Alkanes — only react via H-atom abstraction. They can react with OH and Cl but OH is the dominant oxidant.

Alkenes can react through the C=C via oxidant addition. This is FASTER than H-atom abstraction and so makes alkenes more reactive (better at forming O₃). OH, NO₃ and O₃ can add to alkene C=C bonds. The O₃ reaction leads to the formation of a short-lived primary ozonide, which then breaks up to make Criegee Intermediates. These are best thought of as carbonyl oxides (i.e. zwitterionic compounds).

</details>

**3.** Two oxidation products of limonene have been observed, see below. Show mechanisms that would explain these products. Consider all relevant atmospheric oxidants.

![Limonene oxidation products](media/chapter4_limonene_products.jpeg)

<details>
<summary><b>Show answer</b></summary>

There are many plausible answers for this question. Relevant oxidants are OH, O₃ and NO₃. Not every student needs to go through each oxidant, but more than one should be discussed. The scheme below focuses on OH and O₃. The most difficult product is the second one (limonaldehyde).

![Worked mechanism for limonene oxidation](media/chapter4_limonene_mechanism.png)

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*Make sure you pull people up who move H atoms around. This never happens and we have not discussed it. Reactions with O₂ are very common and so should be considered first. We are dealing with gas phase processes, so the students need to think about simple elementary steps.*

</details>

**4.** This question wants you to think about the atmospheric fate of 1-pentene.

(a) What are the atmospherically important oxidants for 1-pentene?

<details>
<summary><b>Show answer</b></summary>

As with all VOCs, OH, Cl, O₃ and potentially NO₃ are possible. Cl tends to be the most reactive but least abundant. By far the most important during the day is OH; at night it's NO₃, and O₃ plays a lesser role.

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*This is qualitative but can be made quantitative by getting students to think about typical mixing ratios and the rate constants (see the figure in the notes). I would consider going through this to help make it quantitative.*

</details>

(b) Show the reaction mechanism for each important oxidant following through to the appearance of the first stable (closed shell) products. (Consider conditions with and without nitrogen oxide present in the atmosphere.)

<details>
<summary><b>Show answer</b></summary>

![Worked mechanism for 1-pentene oxidation by OH, NO3 and O3](media/chapter4_1-pentene_mechanism.png)

</details>

<details>
<summary><i>Supervisor notes</i></summary>

*Students may end up with slightly different products for the OH and NO₃ reactions if they attack the C2 carbon. That's OK, but structurally unfavoured. May want to talk about which part of the C=C bond they think is more labile. NB we are talking kinetics not thermodynamics, so sterics is important. You can also go more into the decomposition of the CI formed from the reaction with O₃. For CH₂O₂ this hasn't been shown, so it's fine to leave it like that. For the larger ones, RO₂ and OH are formed.*

</details>

**5.** Explain the mechanism of formation of these two products from oxidation of alpha-pinene and explain which oxidants are going to dominate alpha-pinene destruction in a NOx-free tropospheric environment. **[2.5+2.5+2, 2.5 points for each mechanism and 2 for the oxidants]** *(from Tripos 2021, Paper 3 Q44)*

![Alpha-pinene oxidation products](media/chapter4_alphapinene_products.png)

<details>
<summary><b>Show answer</b></summary>

Relevant oxidants are ozone and OH **[2]**.

Reaction mechanism for the first molecule **[2.5]**:

![Alpha-pinene mechanism, first product, step 1](media/chapter4_alphapinene_mech_10.png)
![Alpha-pinene mechanism, first product, step 2](media/chapter4_alphapinene_mech_11.png)

Reaction mechanism for the second molecule **[2.5]**:

![Alpha-pinene mechanism, second product, step 1](media/chapter4_alphapinene_mech_12.png)
![Alpha-pinene mechanism, second product, step 2](media/chapter4_alphapinene_mech_13.png)
![Alpha-pinene mechanism, second product, step 3](media/chapter4_alphapinene_mech_14.png)

</details>

**6.** Explain the mechanism of formation of these two products from oxidation of isoprene (2-methyl-1,3-butadiene) in a polluted environment at nighttime. State which oxidants are relevant in these conditions. **[7]** *(from Tripos 2022, Paper 3 Q43)*

![Isoprene oxidation products, molecule 1](media/chapter4_isoprene_mech_15.png)
![Isoprene oxidation products, molecule 2](media/chapter4_isoprene_mech_16.png)

<details>
<summary><b>Show answer</b></summary>

First product **[2]**:

![Isoprene mechanism, first product, part 1](media/chapter4_isoprene_mech_17.png)
![Isoprene mechanism, first product, part 2](media/chapter4_isoprene_mech_18.png)

Second product **[2]**:

![Isoprene mechanism, second product, part 1](media/chapter4_isoprene_mech_17.png)
![Isoprene mechanism, second product, part 2](media/chapter4_isoprene_mech_19.png)
![Isoprene mechanism, second product, part 3](media/chapter4_isoprene_mech_20.png)

Relevant oxidants at night in a polluted environment are NO₃, OH and O₃ **[3]**.

</details>

*Students will also find past tripos questions since 2015 relevant to the content of this course.*
