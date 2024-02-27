#METODOS

#Criar a classe
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    #criar metodo
    def result(self):
        if self.marks > 500:
            return 'Pass!'
        else:
            return 'Fail!'

#criar o objeto
s1 = Student('Maria', 15, 500)
print(s1.result())
