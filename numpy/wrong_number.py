import numpy as np
lst = np.array([[1, 2, 3, 6], [4, 5, 6, 15], [7, 8, 9, 24], [112, 15, 18, 45]])
lst2 = lst.T 
rows = []
for i in lst:
    s = 0
    for j in range(len(i)):
        s += i[j]
        if j == len(i) - 1:
            if i[j] == s - i[j]:
                rows.append(True)
            else:
                rows.append(False)
columns = []
for i in lst2:
    s = 0
    for j in range(len(i)):
        s += i[j]
        if j == len(i) - 1:
            if i[j] == s - i[j]:
                columns.append(True)
            else:
                columns.append(False)

for i in range(len(rows)):
    for j in range(len(columns)):
        if rows[i] + columns[j] == 0:
            print(lst[i, j])
            break

