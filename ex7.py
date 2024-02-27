#Classe Variaveis

class Student:
    total_marks = 1000
    def __init__(self, name, age, marks, total_marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.total_marks = Student.total_marks

    

s1 = Student('Maria',25, 600, 1000)
s2 = Student('Jose', 15, 500, 1000)
s3 = Student('Laura', 14, 100, 1000)
s4 = Student('Otavio', 18, 250, 1000)
s5 = Student('Luiza', 22, 700, 1000)
s6 = Student('Sergio', 21, 0, 1000)

