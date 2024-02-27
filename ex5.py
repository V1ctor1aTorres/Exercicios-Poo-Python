#METODOS:

#Criar classe
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    #criar metodo
    def result(self):
        if self.marks >= 500:
            return 'PASSS!'
        else:
            return 'FAIL!'
        
#criar objetos       
s1 = Student('Maria', 800)
s2 = Student('Jose', 200)
s3 = Student('Laura', 500)
s4 = Student('Otavio', 350)
s5 = Student('Luiza', 900)
s6 = Student('Sergio', 175)

#lista com os objetos criados
student_objects = [s1, s2, s3, s4, s5, s6]
#lista pass
pass_students = []
#lista fail
fail_students = []
#dicionario com as duas listas
students_result = {}

#Para cada obj na lista de objetos
for s in student_objects:
    #se o resultado do obj é igual a pass entao
    if s.result() == 'PASSS!':
        #adiciona o nome do obj na lista pass
        pass_students.append(s.name)
        #colocar o nome da lista dentro do dicionario
        students_result['Pass students'] = pass_students
    else:
        #adiciona o nome do obj na lista fail 
        fail_students.append(s.name)
        #colocar o nome da lista dentro do dicionario
        students_result['Fail students'] = fail_students


#mostrar o dicionario com as duas listas
print(students_result) 
