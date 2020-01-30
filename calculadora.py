class Calculadora:
    def __init__(self, n1, n2):
        self.n1=n1
        self.n2=n2
    
    def suma(self):
        try:
            total=self.n1+self.n2
            print("La suma de {} y {} es: {}".format(self.n1,self.n2,total))
        except TypeError:
            print("Tipo de dato debe ser numérico")

    def resta(self):
        try:
            resto=self.n1-self.n2
            print("La resta de {} y {} es: {}".format(self.n1,self.n2,resto))    
        except TypeError:
            print("Tipo de dato debe ser numérico")
    
    def multiplicar(self):
        try:
            producto=self.n1*self.n2
            print("La multiplicación de {} y {} es: {}".format(self.n1,self.n2,producto))
        except TypeError:
            print("Tipo de dato debe ser numérico")
    
    def dividir(self):
        try: 
            cociente=round(self.n1/self.n2,2)
            print("La divición de {} y {} es: {}".format(self.n1,self.n2,cociente))
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
        except TypeError:
            print("Tipo de dato debe ser numérico")
        except: 
            print("Error al dividir")
    def sacar_exponente(self):
        try:
            exponente=self.n1**self.n2
            print("El exponente de {} y {} es: {}".format(self.n1,self.n2,exponente))
        except TypeError:
            print("Tipo de dato debe ser numérico")
    
    
