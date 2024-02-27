#Tipos de metodos
class Laptop:                                                                         #CLASS
    discount = 10                                                                     #CLASS VARIABLE
    #default method
    def __init__(self, name, price):
        self.name = name                                                              #CLASS ATRIBUTE
        self.price = price
    
    #o nome do laptop é m6600 e o preço é 12500                                       #CLASS METHOD
    @classmethod
    #clr é o argumento que representa o nome da classe
    def fromString(clr, string):
        #importa expressoes regulares, facilita pegar valores da string
        import re
        item = re.findall('is \w*', string)
        #se refere a m6600
        name = item[0][3:]
        #se refere a 12500
        price = item[1][3:]
        return clr(name, price)


    def applyDiscount(self):                                                          #INSTANCE METHOD
        discount_value = (self.price/100) * self.discount
        final_value = self.price - discount_value
        return int(final_value)



m6600 = Laptop('m6600', 12500)
#Mostra os parametros 
print(m6600.__dict__)
#mostra o desconto de 10%
print(m6600.applyDiscount())
#Muda o desconto para 25%
m6600.discount = 25
#Mostra os parametros novamente
print(m6600.__dict__)
#Mostra o desconto de 25%
print(m6600.applyDiscount())

