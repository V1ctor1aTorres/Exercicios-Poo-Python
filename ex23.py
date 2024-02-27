#Metodo de substituição
class Phone:
    def __init__(self,brand, model, price):
        self.brand= brand
        self.model = model
        self.price = price
        
    @staticmethod
    def make_a_call(phone_num):
        print(f'Calling...{phone_num}')
    def full_name(self):
        return f'{self.brand}, {self.model}, {self.price}'
    
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


p1 = Phone('Nokia', 256, 8000)
sp1 = SmartPhone('Nokia', 256, 8000, 2, 6, 16)
fs1 = FlagShip('Nokia', 256, 8000, 2, 6, 16, 8)
print(p1.full_name())
print(sp1.full_name())
print(fs1.full_name())
