#Abstração e Encapsulamento
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
    

p1 = Phone('Nokia', 32, 350)
print(p1.__dict__)
print(p1.make_a_call('002255'))
