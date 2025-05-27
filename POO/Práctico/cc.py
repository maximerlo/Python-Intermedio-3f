from cb import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0,limite_extraccion = 500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
    
    def extraer(self, monto):
        if monto > self._limite_extraccion:
            print(f"Usted no puede extrar ${monto}, excede el monto permitido. Por favor ingrese otro valor")
        elif monto > self.obtener_saldo():
            print(f"Saldo insuficiente. El monto ${monto} excede el valor que posee en su cuenta, usted tiene ${self.obtener_saldo()}")
        else:
            self._saldo -= monto
            print(f"Se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo acutal es de: {self.obtener_saldo()}")
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo es de: {self._saldo}")
        else:
            print("El monto a depositar debeser mayor a 0")