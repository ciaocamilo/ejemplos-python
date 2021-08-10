numero = 57

# if numero > 0:
#     print("El número es positivo")
# else:
#     if numero < 0:
#         print("El número es negativo")
#     else:
#         if numero == 0:
#             print("El numero es cero")

# if numero > 0:
#     print("El número es positivo")
# elif numero < 0:
#     print("El número es negativo")
# elif numero == 0:
#     print("El numero es cero")

if numero > 0:
    if numero >= 10 and numero <= 99:
        print("El número es positivo y tiene dos dígitos")
    else:
        print("El número es positivo y no tiene dos dígitos")
else:
    if numero >= -999 and numero <= -100:
        print("El número es negativo y tiene tres dígitos")
    else:
        print("El número es negativo y no tiene tres dígitos")

print(type(True))

x = 10
if x%2 == 0 :
    print('x es par')
else :
    print('x es impar')

#Para explicar Try y Except utilizaremos de ejemplo una función que convierte la temperatura en grados Fahrenheit a una temperatura en grados Celsius:

# temperatura_fahr = input('Ingrese la temperatura en grados Fahrenheit: ')
# try:
#     fahr = float(temperatura_fahr)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('El dato debe ser un número')

# x = 6
# y = 2

# print(x >= 2 and (x/y) > 2)
# x = 1
# y = 0
# print(x >= 2 and (x/y) > 2)
# x = 6
# y = 0
# print(x >= 2 and (x/y) > 2)

x = 6
y = 0

print(x >= 2 and y != 0 and (x/y) > 2)