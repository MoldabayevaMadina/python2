import re
dict1 = {}
pattern = r'^[a-z][a-z0-9]*@[a-z]*\.[ru|com]'
n = int(input())
for i in range(n):
    s = input()
    name_and_adress = re.findall("([a-zA-Z][a-zA-Z0-9]*)<(.*)>", s)
    try:
        name, adress = name_and_adress[0]
    except:
        print('enter another name and adress')
        continue
    dict1[adress] = name
list_of_adresses = dict1.keys()     
valid_adresses = [x for x in list_of_adresses if re.findall(pattern, x)]
#print(valid_adresses)
for i in valid_adresses:
    print(dict1[i], i)    
