import random as rd
import string
import re
letters = string.ascii_letters
all = [chr(x) for x in range(48, 58)]
all.extend(letters)
while True:
    s = ''.join(rd.choice(all) for i in range(10))
    if len(re.findall(r'[0-9]', s)) >= 4:
        print(s)
        break