#Name  Mangling
class Phone:
    def __init__(self,brand, model, price):
        self.brand= brand
        self.model = model
        self.__price = price
        
    @staticmethod
    def make_a_call(phone_num):
        print(f'Calling...{phone_num}')
    def __full_name(self):
        return f'{self.brand}, {self.model}, {self.__price}'
    
class SmartPhone(Phone):
    def __init__(self, brand, model, price, ram, memory, camera):

        super().__init__(brand, model, price)
        self.ram = ram
        self.memory = memory
        self.camera = camera
    def __full_name(self):
        return f'{self.brand}, {self.model}'

class FlagShip(SmartPhone):
    def __init__(self, brand, model, price, ram, memory, camera, front_camera):

        super().__init__(brand, model, price, ram, memory, camera)
        self.front_camera = front_camera

p1 = Phone('Nokia', 125, 639)
print(p1._Phone__price)
print(p1.full_name())
