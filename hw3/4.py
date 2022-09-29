import re
list_of_num = ['87053457678', '89094566687', '878978654321', '+7 707 567 8767', '8-705-564-9098', '8-7799097867']
pattern = r'[+7|8][-|\s]?[705|777|776|747|701]{3}[-|\s]?[0-9]{3}[-|\s]?[0-9]{4}'
valid_num = [x for x in list_of_num if re.findall(pattern, x)]
for num in list_of_num:
    if num in valid_num:
        print('YES')
    else:
        print('NO')