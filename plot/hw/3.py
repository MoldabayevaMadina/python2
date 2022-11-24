import matplotlib.pyplot as plt
from math import *
import numpy as np
x = np.linspace(0, 50, num = 200)
y1 = np.cos(x * pi / 25)
y2 = np.sin(x * pi / 25)
y3 = -np.sin(x * pi / 25)
y4 = -np.cos(x * pi / 25)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.grid(True)
plt.show()