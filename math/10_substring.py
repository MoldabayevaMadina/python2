def friendly(p):
    l = [int(i) for i in p]
    if sum(l) == 10:
        return True
    else:
        return False

def is_friendly(s, k, a = False):
    list1 = []
    while k > 1:
        for i in range(len(s)-1):
            if i + k - 1 <= len(s) - 1:
                substr = s[i:i + k]
                if friendly(substr):
                    list2 = list(range(i, i + k))
                    list1.extend(list2)
                    set1 = set(list1)
                    if len(set1) == len(s):
                        return True
        k -= 1
    return False
n = eval(input())
cnt = 0
for i in range(1, 10 ** n + 1):
    if is_friendly(str(i), len(str(i))):
        cnt += 1
print('T(n) = ', cnt)