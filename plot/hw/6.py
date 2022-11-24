import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
theta = np.linspace(-2*np.pi, 2*np.pi, 70)
z = np.linspace(-2, 17, 70)
x = 1.5 * np.sin(theta)
y = 1.5 * np.cos(theta)
ax.plot(x, y, z, color = 'black')
plt.show()