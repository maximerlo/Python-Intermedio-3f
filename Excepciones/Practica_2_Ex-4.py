# Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepciónFileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sinembargo, también intenta crear el archivo si no existe.

try:
    with open("archivodenoseque.txt", "r") as archivo:
        # leer = archivo.read()
        # print(leer)
        print(archivo.read())
except FileNotFoundError:
    print("No existe el archivo buscado. Se  creará uno nuevo")
    with open("archivodenoseque.txt", "x") as archivo:
        archivo.write("Nuevo archivo creado")
    print("Se ha creado 'archivodenoseque.txt' con éxito")

#Otra forma de hacerlo

nombre_archivo= "soy_otro_archivo" 

try:
    archivo = open(f"{nombre_archivo}.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe. Intentando crearlo...")
    archivo = open(f"{nombre_archivo}.txt", "w")
    archivo.write("Este es un nuevo archivo")
finally:
    archivo.close