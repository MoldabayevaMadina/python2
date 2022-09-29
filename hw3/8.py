initials = input()
with open('namelist.txt', 'r') as f:
    all = f.read().split('\n')
    for person in all:
        each = person.split()
        fname = each[0]
        lname = each[-1]
        if len(each) == 3:
            mname = each[1]
        if len(initials) == 3 and initials[0] == fname[0] and initials[1] == mname[0] and initials[2] == lname[0]:
            print(f'{fname} {mname} {lname}')
        elif len(initials) == 2 and len(each) == 2 and initials[0] == fname[0] and initials[1] == lname[0]:
            print(f'{fname} {lname}')
        elif len(initials) == 2 and len(each) == 3 and initials[0] == fname[0] and initials[1] == lname[0]:
            print(f'{fname} {mname} {lname}')    

