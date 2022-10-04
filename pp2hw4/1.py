class Investment:
    def __init__(self, stavka, summa):
        self.stavka = stavka
        self.summa = summa
    def value_after(self, n):
        return self.summa + (self.stavka*0.1)*n
    def __str__(self):
        return f'Summa {self.summa} and stavka {self.stavka}'        

deposit1 = Investment(10, 2000)
print(deposit1.value_after(5))
print(deposit1.stavka)
print(deposit1)