import mysql.connector as mysql 
db = mysql.connect( 
host = "localhost", 
user = "root", 
passwd = "NewPassword", 
database="restaurant" 
) 
cursor = db.cursor() 
query = "INSERT INTO inform (table_number, number_seats, price) VALUES (%s,%s, %s)" 
values = [ 
("1", "2", "5000"), 
("2", "2", "5000"), 
("3", "2", "5000"), 
("4", "2", "5000"), 
("5", "2", "5000"), 
("6", "2", "5000"), 
("7", "2", "5000"), 
("8", "4", "10000"), 
("9", "4", "10000"), 
("10", "4", "10000"), 
("11", "4", "10000"), 
("12", "4", "10000"), 
("13", "4", "10000"), 
("14", "4", "10000"), 
("15", "6", "15000"), 
("16", "6", "15000"), 
("17", "6", "15000"), 
("18", "6", "15000"), 
("19", "6", "15000"), 
("20", "6", "15000") 
] 
cursor.executemany(query,values) 
 
query = "INSERT INTO vip_inform (hall_number, hall_seats,  hal_price) VALUES (%s,%s, %s)" 
values = [ 
("1", "10", "50000"), 
("2", "10", "50000"), 
("3", "15", "70000"), 
("4", "15", "70000"), 
("5", "15", "70000") 
] 
cursor.executemany(query,values) 
 
db.commit()