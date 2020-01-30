import random
from vehiculo import Vehiculo
class Simulador:
    def __init__(self, vehiculos):
        self.vehiculos=vehiculos

    def iniciar_simulacion(self,dias):
        for vehiculo in self.vehiculos:
            print("\n")
            print("VEHICULO {}".format(vehiculo.placa))
            print("\n")
            if not vehiculo.motor.esta_encendido():
                vehiculo.motor.encender()
            for dia in range(1,dias+1):    
                print("---------")
                print("Dia # {}".format(dia))
                print("---------")
                distancia=random.randint(0,100)
                litros=random.randint(30,60)
                if not vehiculo.hay_combustible(distancia):
                    vehiculo.cargar_combustible(litros)
                vehiculo.recorrer_distancia(distancia)
            print(vehiculo.obtener_informe())
