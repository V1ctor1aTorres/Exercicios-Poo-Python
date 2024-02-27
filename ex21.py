#HERANÇA multipla

class A:
    def class_a_method(self):
        return "I'm just a class A method"
    def hello(self):
        return "Hello from class A"
    
class B:
    def class_b_method(self):
        return "I'm just a class B method"
    def hello(self):
        return "Hello from class B"
    
class C(A, B):
    pass


instanceA = A()
instanceB = B()
print(instanceA.class_a_method())
print(instanceB.class_b_method())

instanceC = C()
print(instanceC.class_a_method())
print(instanceC.class_b_method())
print(instanceC.hello())

C.mro()

