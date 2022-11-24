import random
import numpy as np
import matplotlib.pyplot as plt
x1 = random.choices(range(40, 70), k = 50) 
y1 = random.choices(range(50), k = 50)
x2 = random.choices(range(60, 120), k = 50) 
y2 = random.choices(range(90), k = 50) 
x0 = random.choices(range(30), k = 50) 
y0 = random.choices(range(30), k = 50)
plt.title('Matplot scatter plot')
plt.scatter(np.asarray(x0)/100, np.asarray(y0)/100 , color = 'blue',  marker = '.')
plt.scatter(np.asarray(x1)/100, np.asarray(y1)/100, color = 'green',  marker = '.')
plt.scatter(np.asarray(x2)/100, np.asarray(y2)/100, color = 'red',  marker = '.')

plt.show()

