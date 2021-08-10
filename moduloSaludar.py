def saludo(cadena):
    return "Hola {}! ¿cómo estas?".format(cadena)

def Suma_y_resta():
    numero1 = int(input("Ingrese el numero 1 "))
    numero2 = int(input("Ingrese el numero 2 "))
    suma = numero1 + numero2
    resta = numero1 - numero2
    print("La suma del numero1 y el numero2 es de " + str(suma))
    print("La resta del numero1 y el numero2 es de " + str(resta))
