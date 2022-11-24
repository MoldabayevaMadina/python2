import matplotlib.pyplot as plt
import numpy as np
import random as rd
x = (0.02, 0.06, 0.08, 0.12, 0.145, 0.198, 0.24, 0.3, 0.43, 0.44, 0.47, 0.5, 0.58, 0.6)
y = (0.04, 0.11, 0.1, 0.12, 0.2, 0.17, 0.22, 0.32, 0.48, 0.38, 0.48, 0.58, 0.5, 0.6)
plt.scatter(x, y)
k = np.polyfit(x, y, 1)
p = np.poly1d(k)
plt.plot(x, p(x), color = 'red')
plt.title('Best fit line')
plt.show()