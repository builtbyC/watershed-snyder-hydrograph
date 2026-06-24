"""
Reconstruct the 4-hour Snyder Synthetic Unit Hydrograph for the study catchment
directly from the parameters documented in this project (data/snyder_parameters.csv).

This is a transparent, reproducible re-plot of the computed values - run it to
regenerate outputs/synthetic_unit_hydrograph_reconstructed.png.

Usage:
    pip install -r scripts/requirements.txt
    python scripts/plot_synthetic_uh.py
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Documented Snyder parameters (see data/snyder_parameters.csv) ---
A      = 11.209491   # catchment area, sq.km
tp     = 24.0952     # basin lag, h
Qp     = 0.7366      # peak discharge, m^3/s
Tbase  = 84.5662     # base time, h
W50    = 40.4989     # width at 50% of peak, h
W75    = 23.0882     # width at 75% of peak, h
D      = 4           # unit hydrograph duration, h

# Snyder's rule: 1/3 of each width before the peak, 2/3 after.
def widths_about_peak(peak_t, width):
    return peak_t - width / 3.0, peak_t + 2.0 * width / 3.0

t_peak = tp  # peak assumed at the basin lag time

# Control points: (time, discharge) anchored on documented widths.
l50, r50 = widths_about_peak(t_peak, W50)
l75, r75 = widths_about_peak(t_peak, W75)

pts = sorted([
    (0.0,        0.0),
    (l50,        0.50 * Qp),
    (l75,        0.75 * Qp),
    (t_peak,     Qp),
    (r75,        0.75 * Qp),
    (r50,        0.50 * Qp),
    (Tbase,      0.0),
])
xs = [max(0.0, p[0]) for p in pts]
ys = [p[1] for p in pts]

# Smooth interpolation through the control points for a clean UH curve.
t = np.linspace(0, Tbase, 600)
q = np.interp(t, xs, ys)

fig, ax = plt.subplots(figsize=(9, 5.2))
ax.plot(t, q, color="#1f6f8b", lw=2.4, label="4-h Synthetic Unit Hydrograph")
ax.fill_between(t, q, color="#1f6f8b", alpha=0.12)
ax.scatter([t_peak], [Qp], color="#d1495b", zorder=5)
ax.annotate(f"Peak  Qp = {Qp} m$^3$/s\nat tp = {tp} h",
            xy=(t_peak, Qp), xytext=(t_peak + 6, Qp * 0.92),
            fontsize=9, color="#333")

ax.set_title("Snyder Synthetic Unit Hydrograph - Ungauged Bengaluru Catchment "
             f"(A = {A:.2f} km$^2$)", fontsize=12)
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Discharge (m$^3$/s)")
ax.set_xlim(0, Tbase)
ax.set_ylim(0, Qp * 1.15)
ax.grid(True, ls="--", alpha=0.4)
ax.legend(loc="upper right", fontsize=9)
fig.tight_layout()

out = "outputs/synthetic_unit_hydrograph_reconstructed.png"
fig.savefig(out, dpi=150)
print(f"Saved {out}")
