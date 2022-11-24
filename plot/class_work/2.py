import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
x = np.arange(0, 10, 0.25)
y = np.arange(0, 8, 0.25)
x0, y0 = np.meshgrid(x, y)

t0 =  (np.sin(x0 * 0.3) * np.cos(y0 * 0.75) /
    (1 + np.abs(x0 * y0) * 0.05))
fig, axes = plt.subplots()
CS = axes.contour(x0, y0, t0)
axes.clabel(CS, inline = True, fontsize = 10)
plt.show()
