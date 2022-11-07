import random as rd
import string, re
password = ''
all = [chr(x) for x in range(33, 126)]
while True:
    password = ''.join(rd.choice(all) for i in range(10))
    if len(re.findall(r'[A-Z]', password)) >= 2 and len(re.findall(r'[0-9]', password)) >= 1 and len(re.findall(r'[*|)|(|#|@|!]', password)):
        print(password)
        break
 