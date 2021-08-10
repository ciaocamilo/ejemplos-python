numero = 5698

# if numero > 0:
#     print("El número es positivo")
# if numero < 0:
#     print("El número es negativo")
# if numero == 0:
#     print("El número es cero")


# if numero > 0:
#     print("El número es positivo")
# else:
#     if numero < 0:
#         print("El número es negativo")
#     else:
#         if numero == 0:
#             print("El número es cero")


# if numero > 0:
#     print("El número es positivo")
# elif numero < 0:
#     print("El número es negativo")
# elif numero == 0:
#     print("El número es cero")

# if numero > 0:
#     if numero >= 10 and numero <= 99:
#         print("El número es positivo y tiene dos dígitos")
#     else:
#         print("El número es positivo y no tiene dos dígitos")
# else:
#     if numero >= -999 and numero <= -100:
#         print("El número es negativo y tiene tres digitos")
#     else:
#         print("El número es negativo y no tiene tres digitos")

# print(int(32.99999))

# x = 6
# y = 0

# print(x >= 2 and y != 0 and (x/y) > 2)

# temperatura_fahr = input('Ingrese la temperatura en grados Fahrenheit: ')
# fahr = float(temperatura_fahr)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)
def calcularTemperatura():
    try:
        fahr = float(temperatura_fahr)
        cel = (fahr - 32.0) * 5.0 / 9.0
        print(cel)
    except:
        print('El valor ingresado debe ser numérico')

temperatura_fahr = input('Enter Fahrenheit Temperature:')
try:
    calcularTemperatura()
except:
    print('El valor ingresado debe ser numérico')
    calcularTemperatura()