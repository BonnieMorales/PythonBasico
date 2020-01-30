class Vehiculo:
    DISTANCIA_BASE=12
    FACTOR_EMISION_GASOLINA=2.196
    FACTOR_EMISION_DIESEL=2.471
    def __init__(self, placa, color, marca, modelo, combustible, Km, tanque, AC):
        self.placa = placa
        self.color = color
        self.marca = marca 
        self.modelo = modelo
        self.combustible = combustible
        self.Km = Km
        self.tanque = tanque
        self.AC = AC
        self.encendido = False
        self.litros_consumidos=0
    
    # def encender(self):
    #     if self.encendido == False:
    #         self.encendido = True
    #         print("Vehiculo encendido")
    #     else:
    #         print("El vehiculo ya esta encendido")
    
    # def apagar(self):
    #     self.encendido = False
    #     print("Vehiculo apagado")

    def tocar_bocina(self):
        print("Muuu") 
    
    def frenar(self):
        print("frenando")
    
    def combustible(self):
        return self.tanque

    def mostrar_vehiculo(self):
        print ("Placa " + self.placa)
        print ("Color " + self.color)
        print ("Marca " + self.marca)
        print ("Modelo " + self.modelo)
        print ("Combustible " + self.combustible)
        print ("Kilometraje {}".format(self.Km) )
        print ("Estado de tanque {}".format(self.tanque))
        if self.AC == True:
            print ("Tiene aire acondicionado")
        else:
            print ("Sin aire acondicionado")
    
    def cargar_combustible(self, litros):
        self.tanque += litros
        print("Cargando {} litros de combustible".format(litros))
    
    def recorrer_distancia(self, distancia):
        variante = self.obtener_variante()
        if self.motor.esta_encendido():
            if distancia <(self.tanque*variante):
                self.Km += distancia
                total_litros=round(distancia/variante,2)
                self.tanque-=total_litros
                self.litros_consumidos += total_litros
                print("\nRecorriendo {} kilómetros".format(distancia))
            else:
                print("No tiene suficiente combustible")
        else:
            print("El vehiculo está apagado")
    
    def calcular_CO2(self):
        if self.combustible=="gasolina":
            return round(self.litros_consumidos*self.FACTOR_EMISION_GASOLINA,3)
        else:
            return round(self.litros_consumidos*self.FACTOR_EMISION_DIESEL,3) 

    def poner_motor(self, motor):
        self.motor = motor 

    def obtener_variante(self):
        cilindrada=self.motor.obtener_cilindrada()
        if cilindrada == 1000:
            return 12
        elif cilindrada == 2000:
            return 10
        else:
            return 8
    
    def hay_combustible(self, distancia):
        variante=self.obtener_variante()
        if not distancia<(self.tanque*variante):
            return False
        return True

    def obtener_informe(self):
        informe="\n---------------------------"
        informe+="\nINFORME FINAL-EMISION CO2"
        informe+="\n---------------------------"
        informe+="\nUd está conduciendo un vehiculo marca {}, modelo {}, color {}".format(self.marca,self.modelo,self.color)            
        informe+="\nHa recorrido un total de {} km. de distancia".format(self.Km)
        informe+="\nHa consumido un total de {} litros de {}".format(self.litros_consumidos,self.combustible)
        informe+="\nEn su tanque tiene {} litros de {}".format(self.tanque,self.combustible)
        informe+="\nSe emitió a la atmosfera un total de {} Kg de CO2".format(round(self.calcular_CO2(),2))
        return informe