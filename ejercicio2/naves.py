from estrelladelMuerte import EstrellaDeLaMuerte

class NavePequena(EstrellaDeLaMuerte):
    def __init__(self, nombre, vida):
        super().__init__()
        self.nombre = nombre
        self.vida = vida

    def ser_atacada(self):
        if self.vida <= self.vida_inicial:
            print(f"La Estrella de la Muerte ha destruido la Nave Pequeña {self.nombre}.")
            self.vida -= self.vida_inicial
        else:
            print(f"La Estrella de la Muerte no puede destruir {self.nombre}.")

class NaveGrande(EstrellaDeLaMuerte):
    def __init__(self, nombre, vida):
        super().__init__()
        self.nombre = nombre
        self.vida = vida

    def ser_atacada(self):
        if self.vida <= self.vida_inicial:
            print(f"La Estrella de la Muerte ha destruido la Nave Grande {self.nombre}.")
            self.vida -= self.vida_inicial
        else:
            print(f"La Estrella de la Muerte no puede destruir {self.nombre}.")
