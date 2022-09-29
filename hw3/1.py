with open('students.txt', 'r') as f1:
    all = f1.read().split('\n')
    with open('students2.txt', 'w+') as f2:
        for person in all:
            each = person.split('\t')
            fname = each[0][0].upper() + each[0][1:]
            lname = each[1][0].upper() + each[1][1:]
            mail = each[2]
            number = '301-' + each[3]
            f2.write(f'{fname}\t{lname}\t{mail}\t{number}\n')

