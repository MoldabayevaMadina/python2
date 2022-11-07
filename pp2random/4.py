import random as rd
import string
s = ''
letters = string.ascii_letters
for i in range(5):
    s += rd.choice(letters)
print(s)
