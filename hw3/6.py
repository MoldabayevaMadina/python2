import re
n = int(input())
cnt = 1
def valid(card):
    num = re.sub('-', '', card)
    for i in range(1, len(num)):
        if int(num[i]) == int(num[i-1]):
            cnt += 1
            if cnt == 4:
                return False
        else:
            cnt = 1 
    return True              

list1 = []
for i in range(n):
    s = input()
    list1.append(s)
pattern = r'^[4|5|6]\d{3}[-]?\d{4}[-]?\d{4}[-]?\d{4}$'
valid_nums = [x for x in list1 if re.findall(pattern, x) and valid(x)]
#print(valid_nums)
for i in list1:
    if i in valid_nums:
        print('Valid')
    else:
        print('Invalid')    




