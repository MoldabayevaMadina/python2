import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch
fig, axes = plt.subplots()
circle = plt.Circle((0.5, 0.5), 0.5, fill = False)
plt.gca().add_patch(circle)
axes.set_aspect(1)
axes.add_artist(circle)
circle1 = plt.Circle((0.5, 0.25), 0.25, fill = False)
plt.gca().add_patch(circle1)
axes.set_aspect(1)
axes.add_artist(circle1)
circle2 = plt.Circle((0.5, 0.05), 0.05, fill = False)
plt.gca().add_patch(circle2)
axes.set_aspect(1)
axes.add_artist(circle2)
plt.show()
