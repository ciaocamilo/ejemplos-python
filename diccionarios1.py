
# persona = {'nombre': 'Pedro', 'apellido': 'Perez', 'edad': 36}
# print(persona)

# persona['edad'] = 37
# print(persona)

# diccionario = {"total": 55, "descuento": True, 15: "15"}

# print(diccionario)

# diccionarioEjemploExcel ={"nombre":5+2,"telefono":3363692, "edad":33, "ciudad":"Pereira"}

# print(diccionarioEjemploExcel)

# diccionario = dict(total= 55, descuento= True, subtotal= 15)

# print(diccionario)

# usuario = {
#     'nombre': 'Nombre del usuario',
#     'edad' : 23,
#     'curso': 'Curso de Python',
#     'skills':{
#         'programacion' : True,
#         'base_de_datos': False
#     },
#     'No medallas' : 10
# }

# # print(usuario['curso'])
# # print(usuario['skills'])
# print(usuario['skills']['base_de_datos'])

# diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
# print(diccionario)
# print(diccionario.keys())
# print(diccionario.values())

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# versiones.clear()
# print(versiones)

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# otra_versiones = versiones.copy()
# print(versiones == otra_versiones)
# print(versiones)
# print(otra_versiones)

# secuencia = ('python', 'zope', 'plone')
# versiones = dict.fromkeys(secuencia)
# print("Nuevo Diccionario : %s" %  str(versiones))
# print("Nuevo Diccionario : {}".format(str(versiones)))

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones.get('plone'))

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones.items())

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# print(versiones.pop('zope'))
# print(versiones)

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# versiones_adicional = dict(django=2.1)
# print(versiones_adicional)
# versiones.update(versiones_adicional)
# print(versiones)

# usuario = {
#     'nombre': 'Nombre del usuario',
#     'edad' : 23,
#     'curso': 'Curso de Python',
#     'skills':{
#         'programacion' : True,
#         'base_de_datos': False
#     },
#     'No medallas' : 10
# }

# print(len(usuario))

versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
print(versiones)
del versiones["python"]
print(versiones)