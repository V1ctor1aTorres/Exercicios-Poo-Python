#STATIC METHOD

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def printstatement():
        print('Alguma coisa')
    

s1 = Student('Maria', 25)
print(s1.printstatement())