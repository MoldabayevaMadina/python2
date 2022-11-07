import random as rd
n = int(input('length = '))
all = [chr(x) for x in range(33, 126)]
while True:
    s = ''.join(rd.choice(all) for i in range(n))
    if len(set(s)) == len(s):
        print(s)
        break