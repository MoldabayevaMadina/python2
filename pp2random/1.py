import random as rd
n = 0
while n != 3:
    x = rd.randint(100, 999)
    if x % 5 == 0:
        print(x)
        n += 1