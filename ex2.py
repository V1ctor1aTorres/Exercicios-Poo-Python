class Product:
    def __init__(self, procuct_name, brand_name, model_name, price):
        self.procuct_name = procuct_name
        self.brand_nanem = brand_name
        self.model_name = model_name
        self.price = price
        #Adicionar mais atributos
        self.modelwithprice = (f'Model: {model_name}, Price: {price}')


laptop = Product('laptop', 'Dell', 'm4800', 5500)
mobile = Product('Mobile', 'Apple', '15s', 6000)

print(mobile.modelwithprice)


