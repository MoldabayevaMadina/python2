import matplotlib.pyplot as plt
import numpy as np
days = []
marks = [25, 48, 75, 7, 16, 66, 27]
days.extend(25 * ['Mon'])
days.extend(48 * ['Tue'])
days.extend(75 * ['Wed'])
days.extend(7 * ['Thu'])
days.extend(16 * ['Fri'])
days.extend(66 * ['Sat'])
days.extend(27 * ['Sun'])
colors = ['blue', 'cyan', 'green', 'red', 'grey', 'brown', 'orange']
fig, ax = plt.subplots()
cnts, values, bars = ax.hist(days,  alpha = 0.5)
ax.set_xticks(days)

 

for i, (cnt, value, bar) in enumerate(zip(cnts, values, bars)):
    bar.set_facecolor(colors[i % len(colors)])

plt.title('Weekday Data')
plt.show()

