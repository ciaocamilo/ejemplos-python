# from numpy import random as r

# print(r.choice(['Andres','Juan','Pedro', 'Mateo'], size= r.choice([1,2],p=[0.1,0.9]) , p=[0.5,0.2,0.2,0.1], replace=False))


import numpy as np

# a = np.array([34, 25, 7])   # Crear una matriz de rango 1

# print(a)

# print(type(a))            # Prints "<class 'numpy.ndarray'>

# print(a.shape)

# print(a[0], a[1], a[2])

# a[0] = 5                  # Cambiar un elemento de la matriz
# print(a)

# b = np.array([[1,2,3],[4,5,6]])    # Crear una matriz de rango 2
# print(b)
# # print(b.shape)

# print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

# matriz = np.zeros((4,5))   # Crear una matriz de todos los ceros
# print(matriz)

# b = np.ones((3,4))    # Crear un conjunto de todos ellos
# print(b)

# c = np.full((2,5), 7)  # Crear una matriz constante
# print(c)

# d = np.eye(8)         # Crear una matriz de identidad 2x2
# print(d)

# e = np.random.random((2,2))  # Crear una matriz llena de valores aleatorios
# print(e)


# Crear la siguiente matriz de rango 2 con forma (3, 4)
# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11 ]]
# a = np.array([[1,2,3], [5,6,7], [9,10,11]])
# print(a)
# # Usar el rebanado para sacar el subconjunto que consiste en las 2 primeras filas
# # y las columnas 1 y 2; b es el siguiente conjunto de forma (2, 2):
# # [[2 3]
# #  [6 7]]
# print()
# b = a[:2, 1:3]
# print(b)

# print()
# # print(np.fliplr(a))

# print(a[0, 1])   # Prints "2"
# b[0, 0] = 77     # b[0, 0] es la misma pieza de datos que a[0, 1]
# print(a[0, 1])   # Prints "77"

# a = np.array([[1,2], [3, 4], [5, 6]])
# print(a)
# print()
# bool_idx = (a > 2)
# print(bool_idx)
# print()
# print(a[bool_idx])

# print(a[a > 2])

# x = np.array([1, 2])   # Dejar que numpy elija el tipo de datos
# print(x.dtype)

# x = np.array([1.0, 2.0])   # Dejar que numpy elija el tipo de datos
# print(x.dtype)

# x = np.array([1, 2], dtype=np.int64)   # Forzar un tipo de datos en particular
# print(x.dtype)                         # Prints "int64"

# x = np.array([[1,2],[3,4]], dtype=np.float64)
# y = np.array([[5,6],[7,8]], dtype=np.float64)

# print(x)
# print(y)
# print()
# Suma de elementos; ambos producen la matriz
# [[ 6.0  8.0]
#  [10.0 12.0]]
# print(x + y)
# print(np.add(x, y))

# print(x - y)
# print(np.subtract(x, y))

# print(x * y)
# print(np.multiply(x, y))

# print(x / y)
# print(np.divide(x, y))

# print(np.sqrt(x))

# x = np.array([[1,2],[3,4]])
# y = np.array([[5,6],[7,8]])

# v = np.array([9,10])
# w = np.array([11, 12])
# Producto interno de los vectores; ambos producen 219

# print(x)
# print()
# print(y)
# print()
# print(v)
# print()
# print(w)
# print()

# print(v.dot(w))
# print(np.dot(v, w))

# print(x.dot(v))
# print(np.dot(x, v))

# print(x.dot(y))
# print(np.dot(x, y))

# x = np.array([[1,2],[3,4]])
# print(x)
# print()
# print(np.sum(x))  # Calcular la suma de todos los elementos; imprime "10"
# print(np.sum(x, axis=0))  # Calcula la suma de cada columna; imprime "[4 6]"
# print()
# print(np.sum(x, axis=1))  # Calcula la suma de cada fila; imprime "[3 7]

# x = np.array([[1,2], [3,4]])
# print(x)    # Prints "[[1 2]
# print()
# tra = x.T

# Añadiremos el vector v a cada fila de la matriz x,
# almacenando el resultado en la matriz y
# x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# v = np.array([1, 0, 1])


# y = np.empty_like(x)   # Crear una matriz vacía con la misma forma que x

# # Agrega el vector v a cada fila de la matriz x con un bucle explícito
# for i in range(4):
#     y[i, :] = x[i, :] + v
# # Ahora y es lo siguiente
# # [[ 2  2  4]
# #  [ 5  5  7]
# #  [ 8  8 10]
# #  [11 11 13]]
# print(y)


# Añadiremos el vector v a cada fila de la matriz x,
# almacenando el resultado en la matriz y
# x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# vv = np.tile(v, (4, 1))   # Amontonar 4 copias de V una encima de la otra
# print(vv)                 # Prints "[[1 0 1]
#                           #          [1 0 1]
#                           #          [1 0 1]
#                           #          [1 0 1]]"
# y = x + vv  # Agrega x y vv elementalmente
# print(y)  # Prints "[[ 2  2  4
#           #          [ 5  5  7]
#           #          [ 8  8 10]
#           #          [11 11 13]]"

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
# x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# v = np.array([[1, 0],[3, 0]])
# print(v)
# print(3 in np.sum(v,axis=0))
#y = x + v  # Añada v a cada fila de x utilizando la radiodifusión
#print(y)  # Prints "[[ 2  2  4]
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"