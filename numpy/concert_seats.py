import numpy as np
#lst = np.array([[1, 0, 0], [2, 1, 1], [3, 2, 3]])
lst = np.array([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 2, 2], [5, 5, 5, 5, 4, 4], [6, 6, 7, 6, 5, 5]])
lst = lst.T 
seats = []
a = True
for i in lst:
    for j in range(1, len(i)):
        if i[j] <= i[j-1]:
            a = False
            break
print(a)
