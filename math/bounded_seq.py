from math import *
n = eval(input())
l = [2]
dict = {}
def seq(l1, k, t):
    if t != 5:
        a = False
        for j in range(3, (l1[0] + 1) ** k + 1):
            for i in range(len(l1)):
                print(i+1, l1[i], j)
                if (l1[i]) ** k < (j + 1) ** (i+1):
                    a = True
                else:
                    a = False
            if a:
                if k not in dict:
                    dict[k] = 1
                    try:
                        l1[k-1] = j
                    except:
                        l1.append(j)
                    seq(l1, k + 1, t + 1)
                else:
                    l1[k-1] = j
                    dict[k] += 1
                    seq(l1, k + 1, t + 1)
seq(l, 2, 0)
print(dict)
    
