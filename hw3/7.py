import re
list_of_month = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
s = input('Enter date: ')
month = re.findall("^[a-zA-Z]{3}", s)
day_and_year = re.findall("^[a-zA-Z]{3}.*[^1-9]([1-9][0-9]?)[^0-9]*([0-9]{4})", s)
for key in list_of_month:
    if key == month[0].upper():
        mm = list_of_month[key]
try:
    dd, yy = map(int, day_and_year[0])
    assert 0 <= dd <= 12
except:
    print('the format of entered date is incorrect')    
else:
    print(f'{mm}/{dd}/{yy}')