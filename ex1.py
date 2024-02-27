#Classes ajudam a reduzir a redundâmcia de código

#Criação da classe Student
class Student:
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

#Criando o primeiro obj da clas Student
student1 = Student('Ana', 12345, 500)
#Criando o segundo obj da clas Student
student2 = Student('José', 7891011, 600)
#Criando o terceiro obj da clas Student
student3 = Student('Maria', 1213141516, 700)

print(student1.name)
print(student2.roll_num)
print(student3.marks)