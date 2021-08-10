# var1 = 10
# var2 = 30
# var3 = 120
# var4 = 500

# maximo = max(var1, var2, var3, var4)
# print(maximo)

# minimo = min(var1, var2, var3, var4)
# print(minimo)

# help(print)

# x = range(6) #DEVUELVE LOS NUMERO DEL 0 AL 4
# print(list(x))

# def saludar(nombre, apellido):
#     saludo = "Hola " + nombre + " " + apellido
#     return saludo

# el_saludo = saludar("Juan", "Perez")

# print(el_saludo)


# def imprime_Cosas():
#     print("La clase esta genial")   #Se debe explicar de la indentacion de python y de como se ejecutan las instrucciones
#     print('Python es lo maximo')

# # imprime_Cosas()

# def repetir_funciones():
#     imprime_Cosas()
#     imprime_Cosas()

# repetir_funciones()

# def saludar(nombre, mensaje='Hola'):
#     print(mensaje, nombre)

# saludar('Pepe Grillo') # Imprime: Hola Pepe Grillo

def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)
    print('segunda linea')
    print('tercera linea')

saludar(nombre="Juancho", mensaje="Buen día")