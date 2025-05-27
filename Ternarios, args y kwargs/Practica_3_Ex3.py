#Determinar si un número es par o impar

# num = int(input("Por favor ingrese un número: "))

# numParOImpar = "El número es par" if num % 2 == 0 else "El número es impar"

# print(numParOImpar)

#---------------------------------------------------------------------------------------------------

# probando el ejercicio con *args, imprime a medida que analiza cada número

# def parOImpar(*numeros):
#     resultado = [f"{numeros} es par" if numeros%2 == 0 else f"{numeros} es impar" for numeros in lista_int]
#     return resultado

# entrada_num = input("Ingrese los números a analizar separados por espacios: ")
# lista_int = [int(n) for n in entrada_num.split()]

# for num in parOImpar(*lista_int):
#     print(num)

# Probando el ejercicio anterior pero ahora que imprima todos los números pares y después todos los impares


def parOImpar(*numeros):
    par = []
    impar = []
    for num in numeros:
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    #Imprime los resultados en una lista para cada situación
    
    # print(f"Los números pares son: {par}")
    # print(f"Los números impares son: {impar}")
    
    #Usando Map
    print(f"Los números pares son: ", ", ".join(map(str, par)))
    print(f"Los números impares son: ", ", ".join(map(str, impar)))
    #Usando List comprehesion
    print(f"Los números pares son: ", ", ".join([str(n) for n in par]))
    print(f"Los números impares son: ", ", ".join([str(n) for n in impar]))
    

entrada_num = input("Ingrese los números a analizar separados por espacios: ")
lista_num = [int(n) for n in entrada_num.split()]

parOImpar(*lista_num)

