# Escribe un programa que intente dividir dos números. Si el segundo número es cero,captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
num1=int(input("ingrese el dividendo: "))
num2=int(input("ingrese el divisor: "))


try:
    division = num1 / num2
    print(f"Se realizó la operación con éxito, el resultado es: {division}")
except ZeroDivisionError:
    print("Ha ocurrido un error. No se puede dividir por 0")
else:
    print(f"Se realizó la operación con éxito, el resultado es: {division}")
    





