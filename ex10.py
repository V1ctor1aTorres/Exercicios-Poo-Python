class Laptop:
    discount = 10
    sno = 0
    def __init__(self, name, price):
        Laptop.sno += 1
        self.sno = Laptop.sno
        self.name = name
        self.price = price

    def applyDiscount(self):
        discount_total = (self.price/100) * Laptop.discount
        discount_final = self.price - discount_total
        return discount_final

m600 = Laptop('m600', 6000)
m480 = Laptop('m480', 3500)

print(m480.__dict__)
m480.bluetooth = 'yes'
print(m480.__dict__)

print(m600.applyDiscount())

m480.discount = 5
print(m480.__dict__)
print(m480.applyDiscount())