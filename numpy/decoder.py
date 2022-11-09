import string
import numpy as np
letters = string.ascii_lowercase
s = input()
l = list(s)
b = l[:3]
c = l[3:6]
a = l[6:]
b = b[::-1]
c[0] = letters[letters.index(c[0]) - 1]
c[1] = letters[letters.index(c[1]) - 1]
c[2] = letters[letters.index(c[2]) - 1]
if len(a) == 3:
    a[0] = letters[int(a[0]) - 1]
    a[2] = letters[int(a[2]) - 1]
elif len(a) == 4:
    if ord('0') <= ord(a[1]) <= ord('9'):
        p = a[0] + a[1]
        a[0] = letters[int(p) - 1]
        a[1] = a[2]
        a[2:] = letters[int(a[3]) - 1]
    else:
        t = a[2] + a[3]
        a[0] = letters[int(a[0]) - 1]
        a[2:] = letters[int(t) - 1]
else:
    p = a[0] + a[1]
    t = a[3] + a[4]
    a[1] = a[2]
    a[0] = letters[int(p) - 1]
    a[2:] = letters[int(t) - 1]
arr = np.array([a, b, c])
for i in range(3):
    for j in range(3):
        print(arr[i, j], end = '')