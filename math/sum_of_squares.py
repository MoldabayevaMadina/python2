from math import *
#n = int(input('N = '))
#l = []
prime = []
def primes():
    for i in range(2, 150):
        a = True
        for j in range(2, i):
            if i % j == 0:
                a = False 
        if a:
            prime.append(i)

primes()

#S = [i for i in range(int(sqrt(n/2))) if sqrt(n - i * i) == isqrt(n - i * i)]
#print(sum(S))
k = 0
needed_primes = [i for i in prime if (i - 1) % 4 == 0]
for n in needed_primes:
    k += sum([i for i in range(ceil(sqrt(n/2))) if sqrt(n - i * i) == isqrt(n - i * i)])
    #print(n, k)
print(k)