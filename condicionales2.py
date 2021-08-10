
numero = 56

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

if numero > 0:
    if numero >= 10 and numero <= 99:
        print("El número es positivo y tiene dos dígitos")
    else:
        print("El número es positivo y no tiene dos dígitos")
elif numero >= -999 and numero <= -100:
        print("El número es negativo y tiene tres dígitos")
else:
    print("El número es negativo y no tiene tres dígitos")
