class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    def get_price(self, n):
        if n > self.amount:
            print(f'we have only {self.amount}kg of {self.name}')
            return 0
        elif n < 10:
            return self.price
        elif 10 <= n <= 99:
            return self.price * 0.9
        else:
            return self.price * 0.8 
    def make_purchase(self, m):
        if self.get_price(m) != 0:
            k = self.get_price(m)
            self.amount -= m
            return k * m
list_of_products = []
n = int(input('Enter amount of different products: '))

product1 = Product('apples', 220, 250)
product2 = Product('bananas', 90, 230)
product3 = Product('oranges', 120, 275)
product4 = Product('lemons', 80, 235)
product5 = Product('strawberries', 30, 170)
product6 = Product('melons', 200, 310)   

print(f'''We have 
-apples {product1.amount}kg
-bananas {product2.amount}kg 
-oranges {product3.amount}kg
-lemons {product4.amount}kg
-strawberries {product5.amount}kg
-melons {product6.amount}kg
Please make a purchase''')

for i in range(1, n+1):
    name = input(f'enter name of product{i}: ')
    amount = int(input('enter amount in kg: '))
    list_of_products.append([name, amount])
total_price = 0
print(' '*15, 'BILL', ' '*10)
print('Name         Amount        Price(1kg)          Price')
for i in list_of_products:
    if i[0] == product1.name:
        if product1.get_price(i[1]) != 0:
            total_price += product1.get_price(i[1]) * i[1]
            print(i[0], (13 - len(str(i[0])))*' ', i[1], (12 - len(str(i[1])))* ' ', product1.get_price(i[1]), (16 - len(str(product1.get_price(i[1])))) * " ", product1.make_purchase(i[1]))
    elif i[0] == product2.name:
        if product2.get_price(i[1]) != 0:
            total_price += product2.get_price(i[1]) * i[1]
            print(i[0], (13 - len(str(i[0])))*' ', i[1], (12 - len(str(i[1])))* ' ', product2.get_price(i[1]), (16 - len(str(product2.get_price(i[1])))) * " ", product2.make_purchase(i[1]))    
    elif i[0] == product3.name:
        if product3.get_price(i[1]) != 0:
            total_price += product3.get_price(i[1]) * i[1]
            print(i[0], (13 - len(str(i[0])))*' ', i[1], (12 - len(str(i[1])))* ' ', product3.get_price(i[1]), (16 - len(str(product3.get_price(i[1])))) * " ", product3.make_purchase(i[1]))
    elif i[0] == product4.name:
        if product4.get_price(i[1]) != 0:
            total_price += product4.get_price(i[1]) * i[1]
            print(i[0], (13 - len(str(i[0])))*' ', i[1], (12 - len(str(i[1])))* ' ', product4.get_price(i[1]), (16 - len(str(product4.get_price(i[1])))) * " ", product4.make_purchase(i[1]))
    elif i[0] == product5.name:
        if product5.get_price(i[1]) != 0:
            total_price += product5.get_price(i[1]) * i[1]
            print(i[0], (13 - len(str(i[0])))*' ', i[1], (12 - len(str(i[1])))* ' ', product5.get_price(i[1]), (16 - len(str(product5.get_price(i[1])))) * " ", product5.make_purchase(i[1]))
    elif i[0] == product6.name:
        if product6.get_price(i[1]) != 0:
            total_price += product6.get_price(i[1]) * i[1]
            print(i[0], (13 - len(str(i[0])))*' ', i[1], (12 - len(str(i[1])))* ' ', product6.get_price(i[1]), (16 - len(str(product6.get_price(i[1])))) * " ", product6.make_purchase(i[1]))
print(f'Total price                                    {total_price}')     

