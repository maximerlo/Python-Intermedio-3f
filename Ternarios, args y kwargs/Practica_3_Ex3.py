#Determinar si un número es par o impar

num = int(input("Por favor ingrese un número: "))

numParOImpar = "El número es par" if num % 2 == 0 else "El número es impar"

print(numParOImpar)