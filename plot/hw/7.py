import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1 = random.choices(range(500, 1000), k = 3200) 
y1 = random.choices(range(-1500, 0), k = 3200)
z1 = random.choices(range(-1500, 0), k = 3200)
x2 = random.choices(range(1000, 2000), k = 5350) 
y2 = random.choices(range(-1000, 500), k = 5350) 
z2 = random.choices(range(-1000, 500), k = 5350) 
x0 = random.choices(range(2000, 3000), k = 2250) 
y0 = random.choices(range(-500, 0), k = 2250)
z0 = random.choices(range(-500, 0), k = 2250)

plt.title('Matplot scatter plot')
ax.scatter(x0, y0, z0, color = 'purple',  marker = '.', s = 1)
ax.scatter(x1, y1, z1, color = 'green',  marker = '.', s = 1)
ax.scatter(x2, y2, z2, color = 'yellow',  marker = '.', s = 1)
plt.show()