class Motor:
    def __init__(self, numero_serie, cilindrada):
        self.numero_serie = numero_serie
        self.cilindrada = cilindrada
        self.encendido = False

    def encender(self):
        # if not self.encendido:
        #     self.encendido = True

        # else:
        #     print("Ya esta encendido")
        self.encendido=True

    def apagar(self):
        self.encendido = False   

    def esta_encendido(self):
        return self.encendido

    def obtener_cilindrada(self):
        return self.cilindrada
    


