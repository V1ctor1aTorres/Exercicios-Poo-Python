#Herança multinivel

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
    
#Child class
class SmartPhone(Phone):
    def __init__(self, brand, model, price, ram, memory, camera):

        super().__init__(brand, model, price)
        self.ram = ram
        self.memory = memory
        self.camera = camera

"""class SmartPhone2(SmartPhone):
    def __init__(self, brand, model, price, ram, memory, camera,):

        super().__init__(brand, model, price)
        self.ram = ram
        self.memory = memory
        self.camera = camera"""

class FlagShip(SmartPhone):
    def __init__(self, brand, model, price, ram, memory, camera, front_camera):

        super().__init__(brand, model, price, ram, memory, camera, front_camera)
        self.front_camera = front_camera


