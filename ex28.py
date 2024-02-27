#Dunder methods / Magic methods

class Phone:
    def __init__(self,brand, model, price):
        self.brand= brand
        self.model = model
        self.price = price
    #Esse metodo mostra a lista do ojt em vez do local na memoria
        #Mostrar o resultado para o usuário
    def __str__(self):
        return f'Marca do aparelho: {self.brand}\nModelo do aparelho: {self.price} \nPreço: R${self.price}'
    #Mostrar o resultado para o dev
    def __repr__(self):
        return f'phone: {self.brand} {self.model} {self.price}'

p1 = Phone("nokia", 123, 56)
print(p1)
print(repr(p1))