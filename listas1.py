# lista = [1, 2.5, 'DevCode', [5,6], 4]

# print(lista[0]) # 1
# print(lista[1]) # 2.5
# print(lista[2]) # DevCode
# print(lista[3]) # [5,6]
# print(lista[3][0]) # 5
# print(lista[3][1]) # 6
# print('Hicimos este cambio ->',lista[1:4]) # [2.5, 'DevCode']
# print(lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
# print(lista[1::26]) # [2.5, [5, 6]]
# print("Hola Estructura de Lenguajes")

# versiones_plone = [2.5, 6, 4, 5]
# print(versiones_plone)

# versiones_plone.append(6)
# print(versiones_plone)

# print("6 ->", versiones_plone.count(6))
# print(versiones_plone)
# versiones_plone.extend(range(5,7))
# print(versiones_plone)

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
# print(versiones_plone.index(4))
# print(versiones_plone.index(4, 2))

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
# print(versiones_plone)

# versiones_plone.insert(2, 3.7)
# print(versiones_plone)

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]

# print(versiones_plone.pop())

# print(versiones_plone)

# versiones_plone = [2.5, 2.5, 3.6, 4, 5, 6]
# print(versiones_plone)

# versiones_plone.remove(2.5)
# print(versiones_plone)

# versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
# print(versiones_plone)

# versiones_plone.reverse()
# print(versiones_plone)

# versiones_plone = [4, 2.5, 5, 3.6, 2.1, 6]
# print(versiones_plone)

# versiones_plone.sort()
# print(versiones_plone)

# lista = [2, "CMS", True, ["Plone", 10]]
# print(lista, type(lista))

# vocales = 'aeiou'
# for letra in 'hermosa':
#      if letra in vocales:
#             print(letra)

# mensaje = "Hola, como estas tu?"
# # mensaje.split() # retorna una lista
# # ['Hola,', 'como', 'estas', 'tu?']
# for palabra in mensaje.split():
#     print(palabra)

# preguntas = ['nombre', 'objetivo', 'sistema operativo']
# respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']

# for pregunta, respuesta in zip(preguntas, respuestas):
#     print('¿Cual es tu {0}?, la respuesta es: {1}.'.format(
#          pregunta, respuesta))

# help(list)