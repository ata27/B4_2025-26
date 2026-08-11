import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'

# ---------------------------------------------------------------
# Data: (label, lifetime in seconds, spatial scale in metres)
# Grouped to match the three lifetime classes in the original figure
# ---------------------------------------------------------------
# label, y(lifetime,s), x(scale,m), (dx_mult, dy_mult, ha)
short_lived = [
    ("OH",      1,      1,    1.6, 1.0, 'left'),
    ("NO$_3$",  3,      2.2,  1.6, 1.0, 'left'),
    ("HO$_2$",  100,    5,    1.6, 1.0, 'left'),
    ("CH$_3$O$_2$", 550, 8,   2.4, 1.0, 'left'),
]

intermediate = [
    ("C$_5$H$_8$", 3600,       20,   1.6, 1.0, 'left'),
    ("C$_3$H$_6$", 1.4e4,      42,   1.6, 1.0, 'left'),
    ("DMS",        7.0e4,      70,   1.7, 0.72, 'left'),
    ("NOx",        1.3e5,      220,  1.6, 1.05, 'left'),
    ("H$_2$O$_2$", 2.2e5,      280,  1.6, 1.15, 'left'),
    ("SO$_2$",     3.5e5,      600,  1.6, 1.0, 'left'),
    ("Trop O$_3$", 1.1e6,      1200, 1.6, 0.85, 'left'),
    ("Aerosols",   2.2e6,      1200, 1.6, 1.05, 'left'),
    ("CO",         5.0e6,      1200, 1.6, 1.05, 'left'),
]

long_lived = [
    ("CH$_3$Br",       2.2e7,  30000,  1.6, 1.0, 'left'),
    ("CH$_3$CCl$_3$",  1.6e8,  2.0e5,  1.6, 1.0, 'left'),
    ("CH$_4$",         3.0e8,  1.0e6,  1.6, 1.0, 'left'),
    ("N$_2$O",         3.8e9,  2.2e6,  1.6, 1.0, 'left'),
    ("CFCs, CO$_2$",   4.5e9,  8.5e6,  1.5, 1.0, 'left'),
]

# ---------------------------------------------------------------
# Figure & axes layout: main chart on the left, a dedicated blank
# margin on the right for hand-written annotation
# ---------------------------------------------------------------
fig = plt.figure(figsize=(11.5, 7.2), dpi=220)
ax = fig.add_axes([0.09, 0.11, 0.60, 0.74])   # main plot
note_ax = fig.add_axes([0.735, 0.11, 0.245, 0.74])  # annotation margin
note_ax.axis('off')

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(0.6, 6e7)
ax.set_ylim(0.5, 6e9)

# --- background category boxes -----------------------------------------
def draw_box(x0, x1, y0, y1, color):
    rect = mpatches.FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                    boxstyle="round,pad=0,rounding_size=0",
                                    linewidth=0, facecolor=color, zorder=1)
    ax.add_patch(rect)

draw_box(0.8, 22, 0.6, 3500, '#e3e6ea')            # short-lived
draw_box(14, 2.6e4, 1600, 1.3e7, '#e3e6ea')        # intermediate
draw_box(2.0e4, 5e7, 1.0e7, 7e9, '#e3e6ea')        # long-lived

# --- category labels (placed in a clear corner of each box) --------------
ax.text(1.1, 3450, "short-lived\nspecies", fontsize=12, fontweight='bold',
        va='top', ha='left', color='#222')
ax.text(17, 9.5e6, "intermediate\nlifetime species", fontsize=12,
        fontweight='bold', va='top', ha='left', color='#222')
ax.text(2.4e4, 5.6e9, "long-lived\nspecies", fontsize=12, fontweight='bold',
        va='top', ha='left', color='#222')

# --- scatter points + labels ---------------------------------------------
def plot_group(group):
    for label, y, x, dx, dy, ha in group:
        ax.scatter(x, y, s=42, color='black', zorder=3)
        ax.text(x * dx, y * dy, label, fontsize=10.5, va='center', ha=ha,
                zorder=4, color='#111')

plot_group(short_lived)
plot_group(intermediate)
plot_group(long_lived)

# --- axis ticks ------------------------------------------------------------
ax.set_yticks([1, 3600, 86400, 3.1536e7, 3.1536e8, 3.1536e9])
ax.set_yticklabels(['1 s', '1 hr', '1 day', '1 yr', '10 yrs', '100 yrs'],
                    fontsize=11)
ax.set_xticks([1, 100, 1e4, 1e6])
ax.set_xticklabels(['1 m', '100 m', '10 km', '1000 km'], fontsize=11)

ax.tick_params(axis='x', which='major', length=5)

ax.set_ylabel('Time scale (lifetime)', fontsize=13, fontweight='bold')
ax.set_xlabel('Spatial scale', fontsize=13, fontweight='bold', labelpad=14)

ax.grid(True, which='major', axis='y', color='#dddddd', linewidth=0.7, zorder=0)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# --- top brackets: micro / local / regional / global scale ---------------
bracket_y = 8e9
bounds = [1, 25, 2500, 3e5, 4.5e7]
names = ['micro-scale', 'local scale', 'regional scale', 'global scale']
for i, name in enumerate(names):
    x0, x1 = bounds[i], bounds[i + 1]
    ax.annotate('', xy=(x1, bracket_y), xytext=(x0, bracket_y),
                 xycoords='data', textcoords='data',
                 arrowprops=dict(arrowstyle='<->', color='black', lw=1.3),
                 annotation_clip=False)
    ax.plot([x0, x0], [bracket_y * 0.85, bracket_y * 1.15], color='black',
            lw=1.3, clip_on=False)
    xm = np.sqrt(x0 * x1)
    ax.text(xm, bracket_y * 1.55, name, fontsize=10.5, ha='center',
            va='bottom', fontweight='bold', clip_on=False)
ax.plot([bounds[-1], bounds[-1]], [bracket_y * 0.85, bracket_y * 1.15],
        color='black', lw=1.3, clip_on=False)

# --- indicative mixing-time arrows (right of the chart, inside its axes) -
ax.set_xlim(0.6, 2.2e8)
mix_x_vert = 1.1e8   # column for the small vertical double-headed arrows
mix_x_horiz0 = 1.75e8
mix_x_horiz1 = 1.05e8

# vertical double-headed arrows mark a time *band*; horizontal arrows mark
# a single characteristic time pointing at the relevant box edge
mix_bands = [(4.5e9, 3.0e8)]              # ~ decadal band (near long-lived box)
mix_single = [3.1536e7, 8.64e4]           # ~1 yr, ~1 day characteristic times

for ytop, ybot in mix_bands:
    ax.annotate('', xy=(mix_x_vert, ytop), xytext=(mix_x_vert, ybot),
                 arrowprops=dict(arrowstyle='<->', color='black', lw=1.3),
                 annotation_clip=False)

for y in mix_single:
    ax.annotate('', xy=(mix_x_horiz1, y), xytext=(mix_x_horiz0, y),
                 arrowprops=dict(arrowstyle='->', color='black', lw=1.3),
                 annotation_clip=False)

ax.annotate('', xy=(mix_x_horiz1, np.sqrt(mix_bands[0][0] * mix_bands[0][1])),
             xytext=(mix_x_horiz0, np.sqrt(mix_bands[0][0] * mix_bands[0][1])),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.3),
             annotation_clip=False)

ax.text(mix_x_horiz0, 6e9, 'Indicative\nmixing times', fontsize=10.5,
        fontweight='bold', clip_on=False, ha='left')

# --- annotation margin panel ----------------------------------------------
note_ax.set_xlim(0, 1)
note_ax.set_ylim(0, 1)
note_ax.add_patch(mpatches.Rectangle((0, 0), 1, 1, fill=False,
                   edgecolor='#bbbbbb', linewidth=1.2, linestyle=(0, (4, 3))))
note_ax.text(0.06, 0.95, 'Notes / annotations', fontsize=11,
             fontweight='bold', color='#888888', va='top')
for y in np.linspace(0.86, 0.04, 22):
    note_ax.plot([0.05, 0.95], [y, y], color='#e6e6e6', linewidth=0.9)

fig.suptitle('Atmospheric lifetime vs. spatial scale of trace species',
             fontsize=14, fontweight='bold', x=0.39, y=0.985)

fig.savefig('/mnt/user-data/outputs/m2-fig2-2-lifetime-scales-clear.png',
            dpi=220, facecolor='white')
print("saved")
