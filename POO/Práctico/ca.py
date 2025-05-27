from cb import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, interes=0.001):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = interes
        self._acciones = 0
    
    def obtener_saldo(self):
        self._acciones += 1
        return self._saldo
    
    def depositar(self,monto):
        self._acciones += 1
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo es de: {self._saldo}")
        else:
            print("El monto a depositar debeser mayor a 0")
            
    def extraer(self,monto):
        self._acciones += 1
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo acutal es de: {self._saldo}")
        else:
            print(f"Saldo insuficiente. El monto ${monto} excede el valor que posee en su cuenta, usted tiene ${self._saldo}")
            
    def calculo_interes (self):
        interes_ganado =self._saldo * self._tasa_interes * self._acciones
        self._saldo += interes_ganado
        print(f"Se han generado ${interes_ganado:.2f} de interés.")
        return self._saldo