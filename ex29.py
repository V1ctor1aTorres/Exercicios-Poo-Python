#Operator Overloading

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    #metodo para operator overloading
    def __add__(self, other):
        return self.price + other.price
    def __sub__(self, other):
        return self.price - other.price
    def __mul__(self, other):
        return self.price * other.price
    

p1 = Phone('Nokia', 785, 2663)
p2 = Phone('Apple', 672, 985)

print(p1 + p2)
print(p1 - p2)
print(p1 * p2)



