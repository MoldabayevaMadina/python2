from math import *
import random as rd
from itertools import combinations
def needed_triangle(d1, d2, d3):
    if round(d1 * d1, 5) == round(d2 * d2 + d3 * d3 - 2 * d2 * d3 * cos(pi/4), 5) or round(d2 * d2, 5) == round(d1 * d1 + d3 * d3 - 2 * d1 * d3 * cos(pi/4), 5) or round(d3 * d3, 5) == round(d2 * d2 + d1 * d1 - 2 * d2 * d1 * cos(pi/4), 5):
        return True
    else: 
        return False
triangles = []
K = int(input())
X = int(input())
#for i in range(K + 1):
#    for j in range(-X, X + 1):
#        A = [j, j ** 2 / i]
list1 = list(range(1, K + 1))
list2 = list(range(-X, X + 1))
c = comb(len(list2), 3)
#print(c)
values = []
cnt = 0
value1 = combinations(list2, 3)
#print(list(value1))
value2 = list(value1)
for i in list1:
    #print(i, '&&&')
    for j in value2:
        #print(j)
        j = list(j)
        j.sort()
        A = [j[0], j[0] ** 2 / i]
        B = [j[1], j[1] ** 2 / i]
        C = [j[2], j[2] ** 2 / i]
        value = [A, B, C]
        if value not in values:
            d1 = dist(value[0], value[1])
            d2 = dist(value[0], value[2])
            d3 = dist(value[2], value[1])
            if needed_triangle(d1, d2, d3):
                #print(value, '***')
                cnt += 1
            values.append([A, B, C])
#print(values)

print(cnt)