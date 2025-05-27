# Escribe un programa que intente dividir dos números. Si el segundo número es cero,captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
# num1=int(input("ingrese el dividendo: "))
# num2=int(input("ingrese el divisor: "))


# try:
#     division = num1 / num2
#     print(f"Se realizó la operación con éxito, el resultado es: {division}")
# except ZeroDivisionError:
#     print("Ha ocurrido un error. No se puede dividir por 0")
# else:
#     print(f"Se realizó la operación con éxito, el resultado es: {division}")
    

# Otra forma de hacerlo pero con WHILE

def dividir():
    while True:
        try:
            numero = int(input("Por favor ingrese un número: "))
            resultado = 10 / numero
        except ZeroDivisionError:
            print("Ha ocurrido un error. No se puede dividir por 0. Intente nuevamente")
        except ValueError:
            print("Ha ocurrido un error. Debe ingresar un número válido. Intente nuevamente.")
        else:
            print("El resultado es: ", round(resultado, 2))
            print("{:.2f}".format(resultado))#Otra forma de redondear un número
            break
dividir()

def dividir_con_recursividad():
    



