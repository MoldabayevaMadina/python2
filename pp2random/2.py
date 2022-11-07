import random as rd
all = []
while len(all) != 100:
    x = rd.randint(1000000000, 9999999999)
    if x not in all:
        all.append(x)
winners = rd.choices(all, k = 2)
print(winners)
