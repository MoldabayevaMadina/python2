from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from PIL import ImageTk, Image
import re
from datetime import *
import mysql.connector as mysql 
db = mysql.connect( 
    host = "localhost", 
    user = "root", 
    passwd = "NewPassword",
    database = "restaurant"
) 
cursor = db.cursor() 
cursor.execute('SELECT table_number FROM inform')
all_tables = cursor.fetchall()

global now, now_year, now_month, now_day
now = datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day

pattern_num = r'[+7|8][-|\s]?[705|777|776|747|701|707]{3}[-|\s]?[0-9]{3}[-|\s]?[0-9]{4}'
pattern_name = '^[A-Za-z]+$'
def closing():
    answer = mb.askyesno(
        title = "Closing", 
        message = "Are you sure you want to leave?\nEntered data will not be saved.")
    if answer:
        for w in windows:
            w.destroy()

def go_back(prev_window, cur_window):
    cur_window.withdraw()
    prev_window.deiconify()
    prev_window.protocol("WM_DELETE_WINDOW", closing)

def go_to_booking(window_user_name, Ename, Esurname, Enum):
    global name, surname, num, user_name
    name = Ename.get()
    surname = Esurname.get()
    num = Enum.get()
    num1 = re.findall(pattern_num, num)
    name1 = re.findall(pattern_name, name)
    surname1 = re.findall(pattern_name, surname)
    if name == '' or surname == '' or num == '':
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please fill all spaces')
    elif len(num1) == 0:
        mb.showinfo(
            title = 'ERROR', 
            message = 'Incorrect format of telephone number')
    elif len(name1) == 0 or len(surname1) == 0:
        mb.showinfo(
            title = 'ERROR', 
            message = 'Incorrect format of name or surname')
    else:
        user_name = name + ' ' + surname
        print(user_name, num)
        window_user_name.withdraw()
        window_booking = Tk()
        window_booking.title('BOOKING')
        window_booking.geometry('500x400')
        window_booking.wm_geometry("+%d+%d" % (370, 100))
        window_booking.resizable(False, False)
        window_booking["bg"] = "white"
        Label(window_booking, text = 'BOOKING', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40)
        Button(window_booking, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(window_user_name, window_booking)).place(x = 20, y = 360, width = 50, height = 20)

        Button(window_booking, text = 'VIP room', font = ("Arial", 10), background = "bisque", command = lambda: vip(window_booking)).place(x = 80, y = 100, width = 130, height = 90)
        Button(window_booking, text = 'Table', font = ("Arial", 10), background = "light cyan", command = lambda: booking_tables(window_booking)).place(x = 300, y = 100, width = 130, height = 90)
        Button(window_booking, text = 'Cancel booking', font = ("Arial", 10), background = "thistle", command = lambda: cancel_booking(window_booking)).place(x = 190, y = 220, width = 130, height = 90)
        
        windows.append(window_booking)
        window_booking.protocol("WM_DELETE_WINDOW", closing)
        window_booking.mainloop()

def cancel_booking(window_booking): 
    global num 
    a=[] 
    a.append(num) 
    answer = mb.askyesno( 
        title = 'CANCEL BOOKING', 
        message = 'Are you sure you want to cancel booking?' 
    ) 
    if answer: 
        window_booking.withdraw() 
        window_cancel_booking = Tk() 
        window_cancel_booking.title('CANCEL BOOKING') 
        window_cancel_booking.geometry('500x150') 
        window_cancel_booking.wm_geometry("+%d+%d" % (370, 100)) 
        window_cancel_booking.resizable(False, False) 
        window_cancel_booking["bg"] = "white" 
        Label(window_cancel_booking, text = 'Your booking was successfully canceled!', font = ("Arial", 12), background = "white", fg = 'black').place(x = 30, y = 50, width = 400, height = 40) 
        Label(window_cancel_booking, text = 'CANCEL BOOKING', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40) 
        q1="DELETE FROM users2 WHERE phone_number = %s" 
        q2=tuple(a,) 
        print(q1,q2) 
        cursor.execute(q1,q2) 
        #q3="DELETE FROM vip_users WHERE phone_number = %s " 
        #q4=(f"{num}", ) 
        #cursor.execute(q3,q4) 
        db.commit() 
        print(cursor.rowcount, "record(s) deleted") 
        Button(window_cancel_booking, text = 'Go to main window', font = ("Arial", 12), background = "white", command = lambda: go_back(main_window, window_cancel_booking)).place(x = 170, y = 110, width = 150, height = 20) 
 
        windows.append(window_cancel_booking) 
        window_cancel_booking.protocol("WM_DELETE_WINDOW", closing) 
        window_cancel_booking.mainloop()


def booking_tables(window_booking):
    window_booking.withdraw()
    window_tables = Tk()
    window_tables.title('BOOKING')
    window_tables.geometry('500x250')
    window_tables.wm_geometry("+%d+%d" % (370, 100))
    window_tables.resizable(False, False)
    window_tables["bg"] = "white"
    var1 = IntVar()
    #var1.set(1)
    meal = ('breakfast', 'lunch', 'dinner')
    combo = ttk.Combobox(window_tables, values = meal)
    combo.current(0)
    combo.place(x =  30, y = 130)
    Label(window_tables, text = 'Booking tables', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40)
    Button(window_tables, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(window_booking, window_tables)).place(x = 20, y = 210, width = 50, height = 20)
    Label(window_tables, text = 'Choose type of meal:', font = ("Arial", 12), background = "white").place(x = 27, y = 100)
    Label(window_tables, text = 'Enter date(dd-mm-yyyy):', font = ("Arial", 12), background = "white").place(x = 30, y = 70, width = 170, height = 30)
    Edate = Entry(window_tables, font = ("Arial", 12), background = "lavenderblush")
    Edate.place(x = 210, y = 70, width = 160, height = 30)
    Button(window_tables, text = 'Next', font = ("Arial", 10), background = "white", command = lambda: show_tables(window_tables, combo, Edate)).place(x = 430, y = 210, width = 50, height = 20)
  
    windows.append(window_tables)
    window_tables.protocol("WM_DELETE_WINDOW", closing)
    window_tables.mainloop()



def finish_booking_tables(window_show_tables,combo5):
    table_num = combo5.get()
    print(table_num)
    
    print(meal_type, date_table, user_name, num)
    query = 'INSERT INTO users2 (table_number, user_name, phone_number, data, meal) VALUES (%s, %s, %s, %s, %s)'
    values = (table_num, user_name, num, date_table, meal_type)
    cursor.execute(query, values)
    query7 = 'SELECT price FROM inform WHERE table_number = %s'
    value7 = (table_num,)
    cursor.execute(query7, value7)
    price1 = cursor.fetchall()
    global price_for_table
    price_for_table = price1[0][0]
    #print(price_for_table, '*********************8')
    db.commit()

    window_show_tables.withdraw()
    window_finish_booking_tables = Tk()
    window_finish_booking_tables.title('BOOKING')
    window_finish_booking_tables.geometry('500x250')
    window_finish_booking_tables.wm_geometry("+%d+%d" % (370, 100))
    window_finish_booking_tables.resizable(False, False)
    window_finish_booking_tables["bg"] = "white"
    window_finish_booking_tables.protocol("WM_DELETE_WINDOW", closing)
    windows.append(window_finish_booking_tables)
    Label(window_finish_booking_tables, text = f'You succesfully booked table {table_num}\nPrice is {price_for_table}', font = ("Arial", 12), background = "white").place(x = 30, y = 40)
    with open('bill.txt', 'w+') as b:
        b.write(f'User_name is {user_name}\nNumber is {num}\nPrice is {price_for_table}')
    window_finish_booking_tables.mainloop()

def finish_booking_vip(window_show_vip, e2, sum1, list):
    vip_num = e2.get()

    print(date_vip, num_of_people, user_name, num)
    query = 'INSERT INTO vip_users2 (hall_number, vip_name, vip_phone, vip_data) VALUES (%s, %s, %s, %s)'
    values = (vip_num, user_name, num, date_vip)
    cursor.execute(query, values)
    query9 = 'SELECT hal_price FROM vip_inform WHERE hall_number = %s'
    value9 = (vip_num,)
    cursor.execute(query9, value9)
    price2 = cursor.fetchall()
    global price_for_vip
    price_for_vip = price2[0][0]

    db.commit()

    window_show_vip.withdraw()
    window_finish_booking_vip = Tk()
    window_finish_booking_vip.title('BOOKING')
    window_finish_booking_vip.geometry('500x250')
    window_finish_booking_vip.wm_geometry("+%d+%d" % (370, 100))
    window_finish_booking_vip.resizable(False, False)
    window_finish_booking_vip["bg"] = "white"
    window_finish_booking_vip.protocol("WM_DELETE_WINDOW", closing)
    windows.append(window_finish_booking_vip)
    Label(window_finish_booking_vip, text = f'You succesfully booked VIP room {vip_num}\nPrice for Vip room is {price_for_vip}\nFor menu is {sum1}\nTotally {price_for_vip+sum1}', background = "white", font = ('Arial', 15)).place(x = 30, y = 70)
    Button(window_finish_booking_vip, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(window_show_vip, window_finish_booking_vip)).place(x = 20, y = 190, width = 50, height = 20)
    with open('bill.txt', 'w+') as b:
        b.write(f'User_name is {user_name}\nNumber is {num}\nPrice for VIP rooms is {price_for_vip}\nFor menu is {sum1}\nTotally {price_for_vip+sum1}')
        #for i in list:
        #    b.write(i)
        #b.write(f'Price for dishes is {sum1}')
    
    window_finish_booking_vip.mainloop()

def menu(window_show_vip, combo4): 
    window_show_vip.withdraw() 
    window_menu = Tk() 
    window_menu.title('MENU') 
    window_menu.geometry('500x250') 
    window_menu.wm_geometry("+%d+%d" % (370, 100)) 
    window_menu.resizable(False, False) 
    window_menu["bg"] = "white" 
    Label(window_menu, text = 'MENU', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40) 
    windows.append(window_menu) 
    window_menu.protocol("WM_DELETE_WINDOW", closing) 
    
    listbox = Listbox(window_menu,width=25,height=20, selectmode=MULTIPLE)  
    Button(window_menu, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(window_show_vip, window_menu)).place(x = 210, y = 210, width = 50, height = 20) 
 
    listbox.pack(side = LEFT, fill = NONE)  
     
    scrollbar = Scrollbar(window_menu)  
    scrollbar.pack(side = RIGHT, fill = BOTH)  
     
    list=(  
    "Mains:",  
    "Carbonara - 1350",  
    "Beefsteak - 2550",  
    "Chicken stroganoff - 2250",  
    "Salmon fettuccine - 1750",  
    "Spaghetti al Pomodoro - 1200",  
    "Ricotta - 1350",  
    " ",  
    "Salads:",  
    "Greek salad - 1450",  
    "Spinach salad - 1200",  
    "Broccoli salad - 1250",  
    "Eggplant salad - 1300",  
    "Caprese salad - 1200",  
    " ",  
    "Soups:",  
    "Pumpkin soup - 1250",  
    "Chicken soup - 1300",  
    "Creamy soup - 1300",  
    "Meatballs soup - 1450",  
    "Seafood Soup - 1600",  
    " ",  
    "Dessert:",  
    "Tiramisu - 1100",  
    "Red velvet cake - 1500",  
    "Cheesecake - 1650",  
    "Apple pie - 1350",  
    "Chocolate muffin - 1250",  
    " ",  
    "Drinks:",  
    "Green tea - 700",  
    "Black tea - 600",  
    "Latte - 650",  
    "Cola/Fanta/Sprite - 500",  
    "Cappuccino - 750"  
    )  
    a=[] 
     
    def select():  
        sum=0 
        result='' 
        for x in listbox.curselection(): 
            result=result+str(listbox.get(x))+'\n' 
            a.append(result)     
     
        l.config(text=result) 
        #print(a) 
     
        list=str(a[(len(a))-1]).split("\n") 
        #print(list) 
        for x in list: 
            if x!="": 
                print(x) 
                list1=re.findall(r'\d+',x) 
                if list1!=[]: 
                    n=int(list1[0]) 
                    sum=sum+n 
        print(sum) 
        l2=Label(window_menu, text=f'SUM: {sum}')  
        l2.place(x = 310, y = 190)  
        Button(window_menu, text = 'finish\nbooking', font = ("Arial", 10), background = "white", command = lambda: finish_booking_vip(window_menu, combo4, sum, list)).place(x = 420, y = 200) 
     
    def delete():  
        listbox.delete(ANCHOR)  
        l.config(text='')  
     
    for x in list:  
        listbox.insert(END, x)  
     
    B=Button(window_menu,text="SELECT", command=select)  
    B.place(x = 250, y = 50)  
     
    B=Button(window_menu,text="DELETE", command=delete)  
    B.place(x = 370, y = 50) 
     
    l1=Label(window_menu, text='SELECTED')  
    l1.place(x = 305, y = 80) 
     
     
    listbox.config(yscrollcommand = scrollbar.set, font = ("Arial", 10), )  
    scrollbar.config(command = listbox.yview)  
     
    global l  
    l=Label(window_menu, text='')  
    l.place(x = 310, y = 120) 
     
     
     
    window_menu.mainloop()


def vip(window_booking):
    window_booking.withdraw()
    window_vip = Toplevel()
    window_vip.title('VIP ROOMS')
    window_vip.geometry('500x420')
    window_vip.resizable(False, False)
    window_vip["bg"] = "white"
    window_vip.wm_geometry("+%d+%d" % (370, 100))
    window_vip.protocol("WM_DELETE_WINDOW", closing)
    Label(window_vip, text = 'VIP rooms', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40)
    Button(window_vip, text = 'Next', font = ("Arial", 10), background = "white", command = lambda: vip1(window_vip)).place(x = 430, y = 380, width = 50, height = 20)
    Button(window_vip, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(window_booking, window_vip)).place(x = 20, y = 380, width = 50, height = 20)
    im1 = ImageTk.PhotoImage(file = 'image01.jpg')
    im2 = ImageTk.PhotoImage(file = 'image02.jpg')
    im3 = ImageTk.PhotoImage(file = 'image03.jpg')
    Label(window_vip, text = 'VIP room 1, 2', fg = 'black', bg = 'white', font = ('Arial', 13)).place(x=10, y=55)
    Label(window_vip, text = 'VIP room 3, 4', fg = 'black', bg = 'white', font = ('Arial', 13)).place(x=10, y=175)
    Label(window_vip, text = 'VIP room 5', fg = 'black', bg = 'white', font = ('Arial', 13)).place(x=10, y=295)
    Label(window_vip, image = im1).place(x=160, y=55)
    Label(window_vip, image = im2).place(x=145, y=175)
    Label(window_vip, image = im3).place(x=160, y=295)
    Label(window_vip, text = 'Price is 70000tg\n(up to 15 people)', fg = 'black', bg = 'white', font = ('Arial', 10)).place(x=340, y=55)
    Label(window_vip, text = 'Price is 40000tg\n(up to 10 people)', fg = 'black', bg = 'white', font = ('Arial', 10)).place(x=340, y=175)
    Label(window_vip, text = 'Price is 70000tg\n(up to 15 people)', fg = 'black', bg = 'white', font = ('Arial', 10)).place(x=340, y=295)

    window_vip.mainloop()

def show_vip(window_vip1, Enum_of_people, Edate_vip):
    global num_of_people
    num_of_people = Enum_of_people.get()
    global date_vip
    date_vip = Edate_vip.get()
    if num_of_people == '' or date_vip == '':
         mb.showinfo(
            title = 'ERROR',
            message = 'Please fill all spaces'
            )
    else:
        
        num_of_people = int(num_of_people)
        d, m, y = date_vip.split('-')
        
        try:
            date_vip2 = date(int(y), int(m), int(d))
            
            print(date_vip2)
        except:
            mb.showinfo(
                title = 'ERROR',
                message = 'Incorrect date'
                )
            print('error')
        if int(y) < now_year:
            mb.showinfo(
                title = 'ERROR',
                message = 'Incorrect date'
                )
        elif int(y) ==  now_year and int(m) < now_month:
            mb.showinfo(
                title = 'ERROR',
                message = 'Incorrect date'
                )
        elif int(y) ==  now_year and int(m) == now_month and int(d) <= now_day:
            mb.showinfo(
                title = 'ERROR',
                message = 'Incorrect date'
                )
        elif num_of_people > 15 or num_of_people <= 0:
            mb.showinfo(
                title = 'ERROR',
                message = 'Number of people should be between 1 and 15'
                )
            
        else:

            window_vip1.withdraw()
            window_show_vip = Tk()
            window_show_vip.title('CHOOSE')
            window_show_vip.geometry('500x420')
            window_show_vip.resizable(False, False)
            window_show_vip["bg"] = "white"
            window_show_vip.wm_geometry("+%d+%d" % (370, 100))
            windows.append(window_show_vip)
            window_show_vip.protocol("WM_DELETE_WINDOW", closing)
            Label(window_show_vip, text = 'VIP ROOMS', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40)
            Button(window_show_vip, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(window_vip1, window_show_vip)).place(x = 20, y = 380, width = 50, height = 20)
            Button(window_show_vip, text = 'Next', font = ("Arial", 10), background = "white", command = lambda: menu(window_show_vip, combo4)).place(x = 430, y = 380, width = 50, height = 20)
            query0 = 'SELECT hall_number FROM vip_users2 WHERE vip_data = %s'
            value0 = (date_vip,)
            cursor.execute(query0, value0)
            
            busy_vips = cursor.fetchall()
            list_of_vips = []
            query = 'SELECT hall_number FROM vip_inform WHERE hall_seats >= %s'
            value = (num_of_people,) 
            cursor.execute(query, value)
            needed_vips = cursor.fetchall()
            cursor.execute('SELECT * FROM vip_inform')
            vips = cursor.fetchall()
            for i in needed_vips:
                if i not in busy_vips:
                    list_of_vips.append(i)
            hall_seats_vip = []
            price_vip = []
            for i in list_of_vips:
                for j in vips:
                    print(j[0], i[0], j[0] == i[0])
                    if j[0] == i[0]:
                        print(j[1], j[2])
                        hall_seats_vip.append(j[1])
                        price_vip.append(j[2])
            print(hall_seats_vip)
            print(price_vip)

            if len(list_of_vips) != 0:
                for i in range(len(list_of_vips)):
                    Label(window_show_vip,  text= f'     {list_of_vips[i][0]}                                            {hall_seats_vip[i]}                                                 {price_vip[i]}', bg = 'white').place(x = 30, y = 100 + 20 * i)
                Label(window_show_vip, text = 'Choose № of vip room you want to book:', font = ("Arial", 10), background = "white").place(x = 30, y = 250)
                
                var4 = IntVar()
                combo4 = ttk.Combobox(window_show_vip, values = list_of_vips)
                combo4.current(0)
                combo4.place(x =  30, y = 275)

                Label(window_show_vip, text = 'VIP room                     number of peple                          price  ', background = "white", font = ('Arial', 10)).place(x = 40, y = 70)
                    
                Label(window_show_vip, text = 'VIP ROOMS', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40)
                Label(window_show_vip, text = 'Choose VIP room:', background = "white",  font = ('Arial', 11)).place(x = 30, y = 50)
            else:
                Label(window_show_vip, text = 'No free VIP rooms', background = "white", font = ('Arial', 15, 'bold')).place(x = 30, y = 60)
 
            window_show_vip.mainloop()


def show_tables(window_tables, combo, Edate):
    global meal_type, date_table
    meal_type = combo.get()
    date1 = Edate.get()
    if date1 == '':
         mb.showinfo(
            title = 'ERROR',
            message = 'Please fill date'
            )
    else:
        d, m, y = date1.split('-')
        
        try:
            date_table = date(int(y), int(m), int(d))
            
            print(date_table)
        except:
            mb.showinfo(
                title = 'ERROR',
                message = 'Incorrect date'
                )
            print('error')
        if int(y) < now_year:
            mb.showinfo(
                title = 'ERROR',
                message = 'Incorrect date'
                )
        elif int(y) ==  now_year and int(m) < now_month:
            
            mb.showinfo(
                title = 'ERROR',
                message = 'Incorrect date'
                )
        elif int(y) ==  now_year and int(m) == now_month and int(d) <= now_day:
            
            mb.showinfo(
                title = 'ERROR',
                message = 'Incorrect date'
                )
        
        else:
            window_tables.withdraw()
            window_show_tables = Tk()
            window_show_tables.title('CHOOSE')
            window_show_tables.geometry('500x580')
            window_show_tables.resizable(False, False)
            window_show_tables["bg"] = "white"
            window_show_tables.wm_geometry("+%d+%d" % (370, 40))
            windows.append(window_show_tables)
            query = ('SELECT table_number FROM users2 WHERE data = %s and meal = %s')
            value = (date_table, meal_type)
            cursor.execute(query, value)
            busy_tables = cursor.fetchall()
            cursor.execute('SELECT * FROM inform')
            tables = cursor.fetchall()
            print(tables)
            list_of_tables = []
            for i in all_tables:
                if i not in busy_tables:
                    list_of_tables.append(i)
            num_seats_tables = []
            price_tables = []
            for i in list_of_tables:
                for j in tables:
                    print(j[0], i[0], j[0] == i[0])
                    if j[0] == i[0]:
                        print(j[1], j[2])
                        num_seats_tables.append(j[1])
                        price_tables.append(j[2])
            print(num_seats_tables)
            print(price_tables)
            for i in range(len(list_of_tables)):
                
                Label(window_show_tables,  text= f'      {list_of_tables[i][0]}                                                         {num_seats_tables[i]}                                            {price_tables[i]}  ', bg = 'white').place(x = 30, y = 100 + 20 * i)
      
            Label(window_show_tables, text = 'table_number                    number of seats                   price  ', background = "white", font = ('Arial', 10)).place(x = 40, y = 70)
            Button(window_show_tables, text = 'finish\nbooking', font = ("Arial", 10), background = "white", command = lambda: finish_booking_tables(window_show_tables, combo5)).place(x = 420, y = 530)
            Label(window_show_tables, text = 'Choose № of table you want to book:', font = ("Arial", 10), background = "white").place(x = 30, y = 510)

            Label(window_show_tables, text = 'TABLES', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40)
            Label(window_show_tables, text = 'Choose table:', background = "white",  font = ('Arial', 11)).place(x = 30, y = 50)
            #Button(window_show_tables, text = 'Next', font = ("Arial", 10), background = "white", command = lambda: show_tables(window_show_tables)).place(x = 430, y = 370, width = 50, height = 20)
            Button(window_show_tables, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(window_tables, window_show_tables)).place(x = 20, y = 540, width = 50, height = 20)
            var5 = IntVar()
            combo5 = ttk.Combobox(window_show_tables, values = list_of_tables)
            combo5.current(0)
            combo5.place(x =  250, y = 510)

            window_show_tables.protocol("WM_DELETE_WINDOW", closing)
            window_show_tables.mainloop()


def vip1(window_vip):
    window_vip.withdraw()
    window_vip1 = Tk()
    window_vip1.title('VIP ROOMS')
    window_vip1.geometry('500x230')
    window_vip1.resizable(False, False)
    window_vip1["bg"] = "white"
    window_vip1.wm_geometry("+%d+%d" % (370, 100))
    windows.append(window_vip1)
    window_vip1.protocol("WM_DELETE_WINDOW", closing)
    Label(window_vip1, text = 'Enter date(dd-mm-yyyy):', font = ("Arial", 12), background = "white").place(x = 30, y = 70, width = 170, height = 30)
    Edate_vip = Entry(window_vip1, font = ("Arial", 12), background = "lavenderblush")
    Edate_vip.place(x = 210, y = 70, width = 160, height = 30)
    
    Label(window_vip1, text = 'Enter number of people:', font = ("Arial", 12), background = "white").place(x = 30, y = 130, width =170, height = 30)
    Enum_of_people = Entry(window_vip1, font = ("Arial", 12), background = "lavenderblush")
    Enum_of_people.place(x = 210, y = 130, width = 30, height = 30)
    Label(window_vip1, text = 'VIP ROOMS', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40)
    
    Button(window_vip1, text = 'Next', font = ("Arial", 10), background = "white", command = lambda: show_vip(window_vip1, Enum_of_people, Edate_vip)).place(x = 430, y = 190, width = 50, height = 20)
    Button(window_vip1, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(window_vip, window_vip1)).place(x = 20, y = 190, width = 50, height = 20)
    window_vip.mainloop()



def enter():
    main_window.withdraw()
    window_user_name = Tk()
    window_user_name.title('ENTER')
    window_user_name.geometry('500x300')
    window_user_name.wm_geometry("+%d+%d" % (370, 100))
    window_user_name.resizable(False, False)
    window_user_name["bg"] = "white"
    windows.append(window_user_name)
    window_user_name.protocol("WM_DELETE_WINDOW", closing)
    Label(window_user_name, text = 'ENTER', background = "black", fg = 'white', font = ('French Script MT', 22, 'bold')).place(x = 0, y = 0, width = 500, height = 40)
    Label(window_user_name, text = 'Enter name: ', font = ("Arial", 11), background = 'white').place(x = 40, y = 80)
    Label(window_user_name, text = 'Enter surname: ', font = ("Arial", 11), background = "white").place(x = 40, y = 120)
    Label(window_user_name, text = 'Enter contact\nnumber:', font = ("Arial", 11), background = "white").place(x = 40, y = 160)
    Button(window_user_name, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(main_window,window_user_name)).place(x = 20, y = 260, width = 50, height = 20)

    Ename = Entry(window_user_name,  background = "lavenderblush")
    Ename.place(x = 160, y = 80, width = 200, height = 30)
    Esurname = Entry(window_user_name, background = "lavenderblush")
    Esurname.place(x = 160, y = 120, width = 200, height = 30)
    Enum = Entry(window_user_name, background = "lavenderblush")
    Enum.place(x = 160, y = 160, width = 200, height = 30)
    Button(window_user_name, text = 'Next', font = ("Arial", 10), background = "white", command = lambda: go_to_booking(window_user_name, Ename, Esurname, Enum)).place(x = 430, y = 260, width = 50, height = 20)

    window_user_name.mainloop()
    



main_window = Tk()
main_window.title('MAIN WINDOW')
main_window.geometry('500x420')
main_window.resizable(False, False)
main_window["bg"] = "black"
main_window.wm_geometry("+%d+%d" % (370, 100))
windows = [main_window]
im = ImageTk.PhotoImage(file = 'image0.jpg')
Label(main_window, image = im).place(x=-2, y=40)
Label(main_window, text = 'Welcome to Versal', background = 'black', font = ('French Script MT', 22, 'bold'), fg = 'white').place(x=150, y=0)
Button(main_window, text = 'Enter', font = ("Arial", 10), fg = 'white', background = "black", command = lambda: enter()).place(x = 450, y = 5)
Label(main_window, text = 'Adress: st. Satpayev, 35. Contact number: 8-777-606-33-33', font = ("Arial", 10), fg = 'white', background = "black").place(x = 5, y = 380)
main_window.protocol("WM_DELETE_WINDOW", closing)
main_window.mainloop()
