# lista = [1, 2.5, 'DevCode', [5,6], 4]

# print(lista[0]) # 1
# print(lista[1]) # 2.5
# print(lista[2]) # DevCode
# print(lista[3]) # [5,6]
# print(lista[3][0]) # 5
# print(lista[3][1]) # 6
# print('Hicimos este cambio ->',lista[1:4]) # [2.5, 'DevCode']
# print(lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
# print(lista[1:6:2]) # [2.5, [5, 6]]
# print("Hola Estructura de Lenguajes")

# print(lista[1:6:2][1][1]) # [2.5, [5, 6]]

# nombre = "Pepe"
# edad = 25
# listas = [nombre, edad]
# print(listas)

# nombre = "Juan" # Queda la memoria cargada
# print(listas)

# nombres = ["Ana", "Bernardo"]
# edades = [22, 21]
# lista = [nombres, edades]
# print(lista)

# nombres += ["Cristina"]
# print(lista)

# factura = ['pan', 'huevos', 100, 1234]
# print(len(factura) - 1)
# print(factura[-3])
# print(factura[-len(factura)])

# factura[0] = 123
# print(factura)

# versiones_plone = [2.5, 3.6, 4, 5]
# print(versiones_plone)
# [2.5, 3.6, 4, 5]
# versiones_plone.append(6)
# print(versiones_plone)

# versiones_plone = [6, 2.5, 6, 4, 5, 6]
# print(versiones_plone.count(6))

# versiones_plone = [2.1, 2.5, 3.6]
# print(versiones_plone)

# versiones_plone.extend([4, 3, 9])
# print(versiones_plone)

# versiones_plone.extend(range(5,10))
# print(versiones_plone)

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
# print(versiones_plone.index(4))
# print(versiones_plone.index(4, 5))
# print(versiones_plone.index(9))

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
# print(versiones_plone)

# versiones_plone.insert(2, 3.7)
# print(versiones_plone)

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]

# print(versiones_plone.pop())

# print(versiones_plone)

# versiones_plone = [2.1, 2.5, 3.6, 4, 2.5, 6]
# print(versiones_plone)

# versiones_plone.remove(2.5)
# print(versiones_plone)

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
# print(versiones_plone)

# versiones_plone.reverse()
# print(versiones_plone)

# versiones_plone = [4, 2.5, 5, 3.6, 2.1, 6]
# print(versiones_plone)

# versiones_plone.sort(reverse=True)
# print(versiones_plone)

# vocales = 'aeiou'
# for letra in 'hermosa':
#      if letra in vocales:
#             print(letra)

# mensaje = "Hola, como estas tu?"
# # print(mensaje.split()) # retorna una lista

# for palabra in mensaje.split():
#     print(palabra)

# preguntas = ['nombre', 'objetivo', 'sistema operativo']
# respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']

# for pregunta, respuesta in zip(preguntas, respuestas):
#     print('¿Cual es tu {0}?, la respuesta es: {1}.'.format(
#          pregunta, respuesta))

lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
print(lista)

for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])