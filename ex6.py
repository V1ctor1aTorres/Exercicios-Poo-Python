#METODOS

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, discount_value):
        discount = (self.price/100) * discount_value
        final_price = self.price - discount
        return final_price
    
    
laptop = Product('Laptop', 5500)
iphone = Product('Iphone', 7300)
list = [laptop, iphone]
for x in list:
    print(x.discount(20))