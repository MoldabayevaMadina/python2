import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12, 13, 14]
y = [44, 47, 64, 68, 7.5, 27, 55, 11, 28, 67, 77, 56, 34, 87, 4]
my_xticks = [13, 16, 22, 1, 4, 28, 4, 8, 10, 20, 22, 19, 5, 24, 7]
plt.xticks(x, my_xticks)
plt.xlabel('This is the X axis')
plt.ylabel('This is the Y axis')
plt.plot(x, y, marker = '^') 
plt.grid(True)
plt.title('title')
plt.show()