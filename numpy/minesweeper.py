import numpy as np

def change_adj(arr, i1, j1):
    for i in range (i1-1, i1+2):
        for j in range (j1-1, j1+2):
            #print(i, j)
            if 0 <= i < arr.shape[0] and 0 <= j < arr.shape[1]:
                try:
                    #print(i, j)
                    arr[i, j] = str(int(arr[i, j]) + 1)
                except:
                    if arr[i, j] == '-':
                        arr[i, j] = '1'
    
def change(arr):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] == '#':
                change_adj(arr, i, j)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] == '-':
                arr[i, j] = '0'

arr = np.array([['-', '-', '-', '#', '#'], ['-', '#', '-', '-', '-'],['-', '-', '#', '-', '-'],['-', '#', '#', '-', '-'],['-', '-', '-', '-', '-']])
change(arr)
print(arr)