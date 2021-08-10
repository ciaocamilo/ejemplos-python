# s = {1, 2, 3, 4}
# print(s)

# s = {True, 3.14, None, False, "Hola mundo", (1, 2)}

# print(s)

# s1 = set([1, 2, 3, 4])
# s2 = set(range(10))
# print(s1)
# print(s2)

# a = set('Hola Pythonista')
# print(a)

# mi_conjunto = {1, 3, 2, 9, 3, 1}
# print(mi_conjunto)
# for numero in mi_conjunto:
#     print(numero)

# set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
# print(set_mutable1)

# set_mutable1.add(22.000001)
# print(set_mutable1)

# set_mutable1.clear()
# print(set_mutable1)

# set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
# set_mutable2 = set([11, 5, 9, 2, 4, 8])
# print(set_mutable1)
# print(set_mutable2)
# print(set_mutable1.difference(set_mutable2))
# print(set_mutable2.difference(set_mutable1))


# proyecto1 = {'python', 'Zope2', 'ZODB3', 'pytz'}
# print(proyecto1)
# proyecto2 = {'python', 'Plone', 'diazo'}
# print(proyecto2)
# proyecto1.difference_update(proyecto2)
# print(proyecto1)

# paquetes = {'python', 'zope', 'plone', 'django'}
# print(paquetes)
# paquetes.discard('django')
# print(paquetes)

# set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
# set_mutable2 = set([11, 5, 9, 2, 4, 8])
# print(set_mutable1)
# print(set_mutable2)
# print(set_mutable1.intersection(set_mutable2))
# print(set_mutable2.intersection(set_mutable1))

# set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
# set_mutable2 = set([11, 5, 9, 2, 4, 8])
# print(set_mutable1)
# print(set_mutable2)
# print(set_mutable1.isdisjoint(set_mutable2))

# set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
# set_mutable2 = set([11, 5, 9, 2, 4, 8])
# set_mutable3 = set([11, 5, 2, 4])
# print( set_mutable1)
# print(set_mutable2)
# print(set_mutable3)
# print(set_mutable2.issubset(set_mutable1))
# print(set_mutable3.issubset(set_mutable1))

# set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
# set_mutable2 = set([11, 5, 9, 2, 4, 8])
# set_mutable3 = set([11, 5, 2, 4])
# print(set_mutable1)
# print(set_mutable2)
# print(set_mutable3)
# print(set_mutable1.issuperset(set_mutable2))
# print(set_mutable1.issuperset(set_mutable3))

# set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
# set_mutable2 = set([11, 5, 9, 2, 4, 8])
# print(set_mutable1)
# print(set_mutable2)
# print(set_mutable1.symmetric_difference(set_mutable2))

# proyecto1 = {'python', 'plone', 'django'}
# print(proyecto1)
# proyecto2 = {'django', 'zope', 'pyramid'}
# print(proyecto2)
# proyecto1.symmetric_difference_update(proyecto2)
# print(proyecto1)

# set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
# set_mutable2 = set([11, 5, 9, 2, 4, 8])
# print(set_mutable1)
# print(set_mutable2)
# print(set_mutable1.union(set_mutable2))

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a | b)

# version_plone_dev = set([5.1, 6])
# print(version_plone_dev)
# versiones_plone = set([2.1, 2.5, 3.6, 4])
# print(versiones_plone)
# versiones_plone.update(version_plone_dev)
# print(versiones_plone)

# cadena = 'abc'
# print(cadena)
# conjunto = {1, 2}
# conjunto.update(cadena)
# print(conjunto)

# diccionario = {'key': 1, 2:'lock'}
# print(diccionario.items())
# conjunto = {'a', 'b'}
# conjunto.update(diccionario)
# print(conjunto)

# lista = [5, 9, 'hola', False]
# conju = set(lista)
# print(type(lista))
# print(type(conju))
# print(conju)