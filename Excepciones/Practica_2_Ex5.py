# Escribe un programa que intente dividir dos números. Si el segundo número es cero,captura la excepción ZeroDivisionError. Si el primer número es un número no válido,captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

try:
    num1=float(input("Escriba el dividendo: "))
    num2=float(input("Escriba el divisor: "))
    
    division = num1 / num2
    print(f"EL resultado de la división es: {division}")
except ZeroDivisionError:
    print("ERROR. No se puede dividir un número por 0")
except ValueError:
    print("ERROR. El caracter ingresado no es correcto. Ingrese un número.")
