import numpy as np
def count(l, n):
    return len([i for i in l if i == n])
def freq_count(l, lvl, n):
    cnt = count(l, n)
    if lvl in dict:
        dict[lvl] += cnt
    else:
        dict[lvl] = cnt
    for i in l:
        if isinstance(i, list):
            freq_count(i, lvl + 1, n)
dict = {}
res = []
lvl = 0
arr = np.asarray([1, 4, [1, 1], 4, [1, 1, [1, 2, 1, 1], 1]], dtype = object)
freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], lvl, 5)
for i in dict.items():
    res.append(list(i))
print(res)
