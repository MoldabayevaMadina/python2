import random as rd
l = ['s', 'a', 'b', 'f', 'r', 'o', 'p', 't']
n = int(input('length = '))
s = ''.join(rd.choice(l) for i in range(n))
print(s)