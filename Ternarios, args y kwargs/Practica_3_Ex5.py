# Imprimir un mensaje de error si no se pasan suficientes argumentos

def sumar_dos_numeros(*args):
    try:
        resultado = args[0] + args[1]
        print(f"La suma de los dos primeros números es: {resultado}")
    except IndexError:
        print("Error: Debes ingresar al menos dos números.")

entrada = input("Ingrese al menos dos números separados por espacios: ")
numeros = [float(n) for n in entrada.split()]

sumar_dos_numeros(*numeros)
