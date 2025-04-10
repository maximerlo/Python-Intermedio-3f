# Escribe un programa que intente sumar un número y una cadena. Si se produce un errorde tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
num1 = 5
num2 = "asd"

try:
    suma = num1 + num2
except TypeError:
    print("No se puede sumar un número con un texto")
else:
    print(f"El resultado de la suma es:{suma}")