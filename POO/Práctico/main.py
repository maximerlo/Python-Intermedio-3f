from cc import CuentaCorriente
from ca import CuentaAhorro

cc1 = CuentaCorriente("Agostina", 333333, '1990/02/03', 15000)
ca1 = CuentaAhorro("Carlos", 3322211, '1995/01/09', 10000)


cc1.extraer(300)   
cc1.extraer(700)
print(cc1.obtener_saldo())  
cc1.depositar(400)
print(cc1.obtener_saldo())
 
print("---"*20)

print(ca1._acciones) 
print(ca1.obtener_edad())
ca1.depositar(2000) 
print(ca1._acciones)      
ca1.extraer(800)     
print(ca1._acciones) 
print(ca1.calculo_interes())           

