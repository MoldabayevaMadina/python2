import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-1, 1.01, 0.01)
y = [i*i for i in x]
plt.plot(x, y)
plt.show()