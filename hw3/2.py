with open('file1.txt', 'r') as f1:
    all1 = f1.read().split('\n')
    with open('file2.txt', 'r') as f2:
        all2 = f2.read().split('\n')
        with open('file3.txt', 'w+') as f3:
            for i in range(len(all1)):
                f3.write(f'{all1[i]}{all2[i]}\n')
