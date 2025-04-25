#Calcular el promedio de una lista de números usando args y un operador ternario

def calcular_promedio(*args):
    return sum(args) / len(args) if args else "No se ingresaron números"

entrada = input("Ingrese una lista de números separados por espacios: ")

numeros = [float(num) for num in entrada.split()]

resultado = calcular_promedio(*numeros)
print("Promedio: ", resultado)
