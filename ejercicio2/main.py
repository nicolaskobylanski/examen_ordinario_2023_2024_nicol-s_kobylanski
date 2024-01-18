from estrelladelMuerte import EstrellaDeLaMuerte
from naves import NavePequena, NaveGrande
from planetas import Concordia, Ilum, Kamino

estrella = EstrellaDeLaMuerte()
nave_pequena = NavePequena("Nave básica de combate", 200)
nave_grande = NaveGrande("Nave nodriza", 1500)


estrella.atacar_nave_pequena(nave_pequena)
estrella.atacar_nave_grande(nave_grande)


estrella.destruir_planeta(Concordia)
estrella.destruir_planeta(Ilum)
estrella.destruir_planeta(Kamino)
