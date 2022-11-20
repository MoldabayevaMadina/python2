from math import *
from itertools import permutations
k = eval(input())
def count(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        cnt = 0
        list0 = [i for i in range(2, n)]
        list1 = list(permutations(list0))
        for i in list1:
            a = True
            if i[0] > 4 or i[-1] < n - 3:
                a = False
            else:
                for j in range(1, len(i)):
                    if abs(i[j] - i[j-1]) > 3:
                        a = False
            if a:
                cnt += 1
    return cnt
s = 0
for i in range(1, k + 1):
    s += count(i) ** 3
print(s)