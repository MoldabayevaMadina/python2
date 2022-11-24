import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
x1 = (1, 1.3, 1.2, 0, -1, -0.7, -0.2, 0.05, 1.45)
y1 = (1, 1.3, 1.2, 0, -1, -0.7, -0.2, 0.05, 1.45)
z1 = (0, 2, 4, 6, 8, 10, 12, 14, 16)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
theta = np.linspace(-2*np.pi, 2*np.pi, 70)
z = np.linspace(-2, 17, 70)
x = 1.5 * np.sin(theta)
y = 1.5 * np.cos(theta)
ax.scatter(x1, y1, z1)
k = np.polyfit(x, y, 1)
p = np.poly1d(k, z)
ax.plot(x, p(x, y), color = 'red')
print(x)
ax.plot(x, y, z, color = 'black')
plt.show()

'''
import matplotlib.pyplot as plt
import numpy as np
import random as rd
x = (0.02, 0.06, 0.08, 0.12, 0.145, 0.198, 0.24, 0.3, 0.43, 0.44, 0.47, 0.5, 0.58, 0.6)
y = (0.04, 0.11, 0.1, 0.12, 0.2, 0.17, 0.22, 0.32, 0.48, 0.38, 0.48, 0.58, 0.5, 0.6)
plt.scatter(x, y)
k = np.polyfit(x, y, 1)
p = np.poly1d(k)
plt.plot(x, p(x), color = 'red')
plt.show()'''