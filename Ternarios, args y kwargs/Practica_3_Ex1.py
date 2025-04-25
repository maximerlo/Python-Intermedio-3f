# Calcular el mayor de dos números ingresados por teclado usando un operadorternario

num1 = int(input("Por favor ingrese el primer número: "))
num2 = int(input("Por favor ingrese el segundo número: "))

numeroMayor = print(f"El número mayor es el primero, que es: {num1}") if num1 > num2 else print(f"El número mayor es el segundo, que es: {num2}")