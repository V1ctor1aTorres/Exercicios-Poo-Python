#Naming convention

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self._discount = 5
    def aplly_discount(self):
        discounted = (self.price/100)* self._discount
        final_price = self.price - discounted
        return final_price    

p1 = Phone('Nokia', 852, 630)
print(p1.__dict__)
print(p1.model)
print(p1.aplly_discount())
