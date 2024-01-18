from planetas import *

from planetas import Planeta

class EstrellaDeLaMuerte:
    def __init__(self):
        self.vida_inicial = 1000
        self.vida = self.vida_inicial

    def destruir_planeta(self, planeta):
        if self.vida < planeta.volumen:
            print(f"No se puede destruir el planeta {planeta.nombre}.")
        else:
            self.vida -= planeta.volumen
            print(f"Se ha destruido el planeta {planeta.nombre}. La estrella de la muerte tiene {self.vida} puntos de vida.")
            self.reiniciar_vida()

    def reiniciar_vida(self):
        self.vida = self.vida_inicial

    def atacar_nave_pequena(self, nave_pequena):
        nave_pequena.ser_atacada()

    def atacar_nave_grande(self, nave_grande):
        nave_grande.ser_atacada()






