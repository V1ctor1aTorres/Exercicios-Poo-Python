#Issue in class: 
#1 - valor negativo no preço
#2 - Quando muda o preço não impacta na especificaçao completa do atributo

#Cria a classe
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model  = model
        #Se price for negativo, será definido como 0
        self.price = max(price, 0)
        """#Quando o preco for negativo, retorna 0
        if price > 0:
            self.price = price
        else:
            self.price = 0
        self.all = (f'{self.brand}, modelo: {self.model}, R${self.price}')"""

    #Permite acessar o método como um atributo (obj.completeAll) em vez de uma chamada de método (obj.completeAll())
    @property
    def completeAll(self):
        return (f'{self.brand}, modelo: {self.model}, R${self.price}')
    @staticmethod
    #Não acessa atributos da instância, apenas executa alguma lógica relacionada à classe.
    def make_a_call(phone_num):
        print('Calling {phone_num}...')
    #Retorna uma string que combina a marca e o modelo do telefone.
    def full_name(self):
        return (f'{self.brand} {self.model}')
    

p1 = Phone('Nokia', '1100', -5000)

