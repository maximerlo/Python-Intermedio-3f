#Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario

def buscar_palabra(palabra_buscada, *args):
    return f"La palabra '{palabra_buscada}' " + ("está en la lista." if palabra_buscada in args else "no está en la lista.")

entrada = input("Ingrese una lista de palabras separadas por espacios: ")
palabras = entrada.split()

palabra = input("Ingrese la palabra a buscar: ")

resultado = buscar_palabra(palabra, *palabras)
print(resultado)
