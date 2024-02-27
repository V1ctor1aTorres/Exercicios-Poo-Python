#Polymorphism

class Phone:
    def __init__(self,brand, model, price):
        self.brand= brand
        self.model = model
        self.price = price
    def full_name(self):
        return f'{self.brand}, {self.model}'    
    def __add__(self, other):
        return f'{self.brand}, {self.model} ' + f'{other.brand}, {other.model} '     


    
class SmartPhone(Phone):
    def __init__(self, brand, model, price, ram, memory, camera):

        super().__init__(brand, model, price)
        self.ram = ram
        self.memory = memory
        self.camera = camera
    def full_name(self):
        return f'{self.brand}, {self.model}'

class FlagShip(SmartPhone):
    def __init__(self, brand, model, price, ram, memory, camera, front_camera):

        super().__init__(brand, model, price, ram, memory, camera)
        self.front_camera = front_camera


p1 = Phone('Nokia', 123, 56987)
sp1 = SmartPhone('Apple', 456, 9101213, 2, 5, 9)
fs1 = FlagShip('Samsung', 789, 1257, 9, 7, 4, 6)
fs2 = FlagShip('Samsung', 789, 1257, 9, 7, 4, 6)

print(p1.__dict__)
print(sp1.__dict__)
print(fs1.__dict__)
print(fs1 + fs2)
