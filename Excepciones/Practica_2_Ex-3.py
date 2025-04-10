# Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
dic={
    "a":1,
    "b":2,
    "c":"zapato"
}

try:
    valor= dic["d"]
except KeyError:
    print("La clave no existe")
else:
    print(f"El valor asignado es: {valor}")