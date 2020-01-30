from vehiculo import Vehiculo
from simulador import Simulador
from motor import Motor

m1 = Motor("739390",1000)
m2 = Motor("139488",2000)

v1 = Vehiculo("2809KJG", "Blanco", "Jeep", "2012", "gasolina", 1007, 0, True)
v2 = Vehiculo("8746DLR", "Azul", "Toyota", "2019", "diesel", 500, 80, True)
v3 = Vehiculo("7280YEU", "Gris", "Nissan", "2007", "dsel", 2050, 20, False) 

v1.poner_motor(m1)
v2.poner_motor(m2)
v3.poner_motor(m2)

vehiculos=[v1,v2,v3]

simulador = Simulador(vehiculos) #objeto simulador

simulador.iniciar_simulacion(1)