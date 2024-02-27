#HERANÇA incomum
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
    def __init__(self,brand, model, price, ram, memory, camera):

        Phone.__init__(self,brand, model, price)
        self.ram = ram
        self.memory = memory
        self.camera = camera


p1 = Phone('Nokia', 552, 350, )
print(p1.__dict__)
sp = SmartPhone('Apple', '15s', 5000, '5Gb', '4Gb', '18px')
print(sp.__dict__)