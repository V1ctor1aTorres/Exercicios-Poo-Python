class Laptop:
    def __init__(self, name, price):
        self.name = name
        self.price = price

m600 = Laptop('m600', 6000)
m480 = Laptop('m480', 3500)

print(m480.__dict__)
m480.bluetooth = 'yes'
print(m480.__dict__)