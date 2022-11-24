import random
import numpy as np
import matplotlib.pyplot as plt
x = random.choices(np.arange(0, 1.2, 0.01), k = 50) 
y = random.choices(np.arange(0, 1.2, 0.01), k = 50)
area = random.choices(np.arange(0, 350, 10), k = 50)
colors = ['blue', 'cyan', 'green', 'red', 'black'] * 10
plt.scatter(x, y, s = area, color = colors, alpha = 0.5, edgecolor = 'black')
plt.show()