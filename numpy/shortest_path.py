import numpy as np
def path(i0, j0, arr, k):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] == k:
                d.append(abs(i - i0) + abs(j - j0))
                path(i, j, arr, str(int(k) + 1))
                
d = []
arr = np.array([])
l = [
  ("00000"),
  ("01006"),
  ("02000"),
  ("30050"),
  ("00004")
]

l1 = []
for i in l:
    l1.append(list(i))
arr = np.asarray(l1)
cnt = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i, j] == '1':
            path(i, j, arr, '2')
print(sum(d))