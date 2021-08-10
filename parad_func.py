# def suma(val1 = 0, val2 = 0):
#     return val1 + val2

# def resta(val1 = 0, val2 = 0):
#     return val1 - val2

# def operacion(funcion, val1 = 0, val2 = 0):
#     return funcion(val1, val2)

# # funcion_suma = suma
# resultado = operacion(suma, 10, 20)
# print(resultado)

# # funcion_resta = resta
# resultado = operacion(resta, 10, 20)
# print(resultado)


# suma = lambda val1 = 0, val2 = 0 : val1 + val2
# resta = lambda val1 = 0, val2 = 0 : val1 - val2
# operacion = lambda operador, val1 = 0, val2 = 0 : operador(val1, val2)

# resultado = operacion(suma, 10, 20)
# print(resultado)

###################################################################

# def cuadrado(elemento = 0):
#     return elemento * elemento

# lista = [1,2,3,4,5,6,7,8,9,10]

# # resultado = list(map(cuadrado, lista))
# # print(resultado)

# resultado = list(map(lambda elemento : elemento * elemento, lista))
# print(resultado)

# def mayor_a_cinco(elemento):
#     return elemento > 5

# tupla = (5,2,6,7,8,10,77,55,2,1,30,4,22,3)

# # resultado  = tuple(filter(mayor_a_cinco, tupla))
# # print(resultado)

# resultado = tuple(filter(lambda elemento: elemento > 4, tupla))
# print(resultado)

# from functools import reduce

# lista = [1,2,3,4]

# def funcion_acumulador(acumulador= 0, elemento = 0):
#     return acumulador + elemento

# resultado = reduce(funcion_acumulador, lista)
# print(resultado)

# from functools import reduce

# lista = ['Python', 'Java', 'Ruby', 'Elixir']
# resultado = reduce(lambda acumulador = 0, elemento = '' : acumulador + ' - ' + elemento, lista)
# print(resultado)


# items = [1, 2, 3, 4, 5]
# suma10 = reduce(lambda x, y : x + y, items, 10)
# print(suma10)

# nombres = ["Raul", "Pedro", "Sofia"]
# apellidos = ["Lopez Briega", "Perez", "Gonzalez"]

# nombreApellido = list(zip(nombres, apellidos))
# print(nombreApellido)

# print('Valido' if True else 'Invalido')