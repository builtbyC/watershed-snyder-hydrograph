# Results & Analysis — Snyder Parameter Calculations

The Snyder synthetic unit hydrograph is built from the physiographic parameters
(area, longest stream length, centroid length) together with the regional
constants C_t and C_p adopted from a hydro-meteorologically homogeneous region.

## Inputs

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Catchment area | A | 11.209 km² |
| Longest stream length | L | 3.82 km |
| Centroid length | L꜀ | 2.13 km |
| Peaking coefficient | C_p | 0.57 |
| Design UH duration | D′ | 4 h |

## Formulas

- Basin lag: `t_p = C_t · (L·L꜀)^0.3`
- Standard duration: `D = 211 · t_p`
- Modified basin lag: `t_p′ = t_p + (D′ − D)/4`
- Peak discharge: `Q_p′ = (2.778 · A · C_p) / t_p′`
- Discharge per unit area: `q_p′ = Q_p′ / A`
- Base time: `T′ = 5.556 / q_p′`
- Width at 50% peak: `W₅₀ = 2.14 · (q_p′)^−1.08`
- Width at 75% peak: `W₇₅ = 1.22 · (q_p′)^−1.08`

Snyder's convention places one-third of each width before the peak and two-thirds after.

## Worked results

Taking the UH duration D′ = 4 h with the peak assumed at 24 h:

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Basin lag | t_p | 24.0952 | h |
| Regional constant | C_t | 12.8468 | – |
| Peak discharge | Q_p′ | 0.7366 | m³/s |
| Discharge per unit area | q_p′ | 0.0657 | m³/s/km² |
| Base time | T′ | 84.5662 | h |
| Width at 50% peak | W₅₀ | 40.4989 | h |
| Width at 75% peak | W₇₅ | 23.0882 | h |

With Q_p′, t_p′, T′, W₅₀ and W₇₅ established, a smooth unit hydrograph giving
1 cm of runoff is sketched — the 4-hour Synthetic Unit Hydrograph for the
catchment. See [`../figures/graph_4-2-1_synthetic_unit_hydrograph.jpeg`](../figures/graph_4-2-1_synthetic_unit_hydrograph.jpeg)
for the project hydrograph, and run `scripts/plot_synthetic_uh.py` to regenerate
it from these values.

## Conclusion

A unit hydrograph for an ungauged catchment was successfully developed using
Snyder's method, driven entirely by GIS-derived physiographic parameters. The
approach allows flood-response estimation for basins that lack rainfall and
streamflow gauges, supporting flood-warning and water-management applications.
