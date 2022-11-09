import string
import numpy as np
def check(s):
    if len(s) != 9:
        return False
    for i in s:
        if ord(i) < ord('a') or ord(i) > ord('z'):            
            return False
    return True

s = input()
letters = string.ascii_letters
if check(s):
    a = list(s[:3])
    b = list(s[5:2:-1])
    c = list(s[6:])
    a[0] = str(letters.index(a[0]) + 1)
    a[2] = str(letters.index(a[2]) + 1)
    c[0] = letters[(letters.index(c[0]) + 1) % 26]
    c[1] = letters[(letters.index(c[1]) + 1) % 26]
    c[2] = letters[(letters.index(c[2]) + 1) % 26]
    arr = np.array([b, c, a])
    for i in range(3):
        for j in range(3):
            print(arr[i, j], end = '')
else:
    print('BANG! BANG! BANG!')
        
        
