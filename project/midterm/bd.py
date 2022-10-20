import mysql.connector as mysql 
db = mysql.connect( 
    host = "localhost", 
    user = "root", 
    passwd = "NewPassword",
    database = "restaurant"
) 
cursor = db.cursor() 
#cursor.execute("CREATE DATABASE restaurant") 
#cursor.execute("CREATE TABLE inform (table_number int, number_seats int, price int)") 
#cursor.execute("CREATE TABLE vip_inform (hall_number int, hall_seats int,  hal_price int )") 
#query = "INSERT INTO users (table_number, user_name, phone_number,data,meal) VALUES (%s,%s, %s,%s,%s)" 
#value = (f"", "10", "50000") 
#cursor.executemany(query,values) 
#cursor.execute("CREATE TABLE users2 (table_number int, user_name VARCHAR (255), phone_number VARCHAR (255), data VARCHAR (255), meal VARCHAR (255) )") 
#cursor.execute("CREATE TABLE vip_users2 (hall_number int, vip_name VARCHAR (255), vip_phone VARCHAR (255), vip_data VARCHAR (255))") 

db.commit()
