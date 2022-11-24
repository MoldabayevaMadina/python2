import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

# make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)

# pie chart parameters
share = [0.210, 0.303, 0.177, 0.107, 0.102, 0.102]
countries = ['Other', 'Italy', 'Ireland', 'Iceland', 'Greece', 'Germany']

# rotate so that first wedge is split by the x-axis
angle = -180 * share[0]
wedges, *_ = ax1.pie(share, autopct='%1.1f%%', startangle=angle,
                     labels=countries)

# bar chart parameters
ratios = [0.36, 0.38, 0.41, 0.42, 0.53]
labels = ['Austria', 'Belgium', 'Denmark', 'Finland', 'France']
bottom = 1
width = .2

for j, (height, label) in enumerate(reversed([*zip(ratios, labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.125 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')


ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)

theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r
bar_height = sum(ratios)

x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-0.1, 1), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(1)
ax2.add_artist(con)

x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-0.1, -1.09), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(1)
plt.legend()
plt.show()