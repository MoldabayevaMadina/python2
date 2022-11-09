import numpy as np
lst = np.array([1, 1, 0, 0, 0, 1, 0])
cnt = 0
if lst[0] == 0:
    print('0')
else:
    for i in range(len(lst)):
        if lst[i] == 1:
            cnt += 1
            lst = (lst + 1) % 2
            #print(lst)
    print(cnt)
