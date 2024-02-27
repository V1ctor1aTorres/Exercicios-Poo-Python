#Defina a classe circle com 2 metodos circunferencia e area

#Cria a classe
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    #Metodo 
    def Circumference(self):
        valor_circumference = 2*Circle.pi*self.radius
        return valor_circumference
    #Metodo
    def Area(self):
        valor_area = Circle.pi*self.radius*2
        return valor_area

#Objetos da classe Circle
c1 = Circle(23)
c2 = Circle(24)

#Mostra a circunferencia
print(c1.Circumference())
#Mostra a area
print(c2.Area())


