from math import *
n = eval(input('n = '))
list1 = [i for i in range(1, n + 1)] 
cnt = 0
for a in list1:
    for b in list1:
        for c in list1:
            if a <= b <= c:
                if a + b > c and a + c > b and b + c > a:
                    if 0.5 * sqrt(2 * a ** 2 + 2 * b ** 2 - c ** 2) == int(0.5 * sqrt(2 * a ** 2 + 2 * b ** 2 - c ** 2)):
                        cnt += 1 
print(cnt)



