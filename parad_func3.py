def suma (val1 = 0, val2 = 0):
    return val1 + val2

# def resta (val1 = 0, val2 = 0):
#     return val1 - val2

# def multiplicacion (val1 = 0, val2 = 0):
#     return val1 * val2


# def operacion (funcion, val1 = 0, val2 = 0):
#     return funcion(val1, val2)

# # funcion_suma = suma
# # funcion_resta = resta
# resultado = operacion(multiplicacion, 10, 20)
# print(resultado)



# def crear_Funcion(operador):
#     if operador == '+':
#         def suma(val1 = 0, val2 = 0):
#             return val1 + val2
#         return suma
#     if operador == '-':
#         def resta(val1 = 0, val2 = 0):
#             return val1 - val2
#         return resta

def operacion (funcion, val1 = 0, val2 = 0):
    return funcion(val1, val2)


# operador = input('seleccione la operación: (+, -) ')
# num1 = int(input('Digite el número 1: '))
# num2 = int(input('Digite el número 2: '))
# # funcion_elegida = crear_Funcion(operador)
# resultado = operacion(crear_Funcion(operador), num1, num2)
# print(resultado)


# suma = lambda val1, val2 : val1 + val2
# operacion = lambda operador, val1, val2 : operador(val1, val2)
# resultado = operacion(suma, 10, 20)
# print(resultado)

# total = lambda precio, cantidad : precio * cantidad
# descuento = lambda total : total - (total * 0.3)
# print(descuento(total(1200, 5)))


# def suma(num1, num2):
#     return num1 + num2

# con_asterisco = lambda *args : args[1]

# print(con_asterisco('hola', 'mundo', 'hoy'))

# con_doble_asteristo = lambda **kwargs : kwargs.get('apellido')


# print(con_doble_asteristo(nombre='Pedro', apellido='Gomez'))


########################################

# def cuadrado(elemento = 0):
#     return elemento * elemento

# lista = [1,2,3,4,5,6,7,8,9,10]

# resultado = list(map(cuadrado, lista))
# print(resultado)

# resultado = set(map(lambda elemento : elemento * elemento, lista))
# print(resultado)


# def mayor_a_cinco(elemento):
#     return elemento > 5

# tupla = (5,2,6,7,8,10,77,55,2,1,30,4,22,3)

# resultado  = tuple(filter(mayor_a_cinco, tupla))
# print(resultado)


# resultado = tuple(filter(lambda elemento: elemento > 5, tupla))
# print(resultado)

from functools import reduce

# lista = [1,2,3,4]

# # def funcion_acumulador(acumulador= 0, elemento = 0):
# #     return acumulador + elemento

# # resultado = reduce(funcion_acumulador, lista)
# # print(resultado)

# resultado = reduce(lambda acumulador = 0, elemento = 0 : acumulador + elemento, lista)
# print(resultado)

# lista = ['Python', 'Java', 'Ruby', 'Elixir']
# resultado = reduce(lambda acumulador = 0, elemento = '' : acumulador + ' - ' + elemento, lista)
# print(resultado)

# items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# suma10 = reduce(lambda x, y : x + y, items, 10)
# print(suma10)

# nombres = ["Raul", "Pedro", "Sofia"]
# apellidos = ["Lopez Briega", "Perez", "Gonzalez"]

# nombreApellido = list(zip(nombres, apellidos))
# print(nombreApellido)
a = 15
print('Valido' if a > 10 else 'Invalido')