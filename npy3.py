import numpy as np

# a = np.array([34, 25, 7])   # Crear una matriz de rango 1
# print(a)

# a[0] = 5                  # Cambiar un elemento de la matriz

# print(a)

# b = np.array([[1,2,3],[4,5,6]])
# print(b)
# print()
# # print(np.shape(b))

# print(b[0, 0], b[0, 1], b[1, 0])

# matriz = np.zeros((4,6))
# print(matriz)

# b = np.ones((3,2))    # Crear un conjunto de todos ellos
# print(b)

# c = np.full((2,5), 9)
# print(c)

# d = np.eye(8)
# print(d)

# d[3, 4] = 4

# print()
# print(d)

# e = np.random.random((2,2))
# print(e)

# a = np.array([[1,2,3], [5,6,7], [9,10,11]])
# print(a)
# print()
# # Usar el rebanado para sacar el subconjunto que consiste en las 2 primeras filas
# # y las columnas 1 y 2; b es el siguiente conjunto de forma (2, 2):
# # [[2 3]
# #  [6 7]]
# b = a[:2, 1:3]
# print(b)
# b[0, 0] = 77
# print()
# print(a)


# a = np.array([[1,2], [3, 4], [5, 6]])
# a = np.array([[1,2], [3, 4], [5, 6]])
# # Un ejemplo de indexación de arreglos enteros.
# # La matriz devuelta tendrá forma (3,2) y
# print(a)
# print()
# # print(a.shape)
# # print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"
# # bool_idx = (a > 2)
# # print(bool_idx)
# print()
# # print(a[bool_idx])

# print(a[a > 2])

# x = np.array([1, 2])   # Dejar que numpy elija el tipo de datos
# print(x.dtype)

# x = np.array([[1,2],[3,4]], dtype=np.float64)
# y = np.array([[5,6],[7,8]], dtype=np.float64)
# # Suma de elementos; ambos producen la matriz
# # [[ 6.0  8.0]
# #  [10.0 12.0]]
# print(x)
# print()
# print(y)
# print()
# print(x + y)
# print()
# print(np.add(x, y))

# print(x - y)
# print()
# print(np.subtract(x, y))

# print(x * y)
# print()
# print(np.multiply(x, y))

# print(x / y)
# print()
# print(np.divide(x, y))

# print(np.sqrt(x))

# x = np.array([[1,2],[3,4]])
# y = np.array([[5,6],[7,8]])
# v = np.array([9,10])
# w = np.array([11, 12])

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
# print(np.sum(x))  # Calcular la suma de todos los elementos; imprime "10"
# print(np.sum(x, axis=0))  # Calcula la suma de cada columna; imprime "[4 6]"
# print(np.sum(x, axis=1))  # Calcula la suma de cada fila; imprime "[3 7]"


# x = np.array([[1,2,8], [3,4,9]])
# print(x)    # Prints "[[1 2]
#             #          [3 4]]"
# print()
# print(x.T)  # Prints "[[1 3]
#             #          [2 4]]"


# Añadiremos el vector v a cada fila de la matriz x,
# almacenando el resultado en la matriz y
# x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# y = np.empty_like(x)   # Crear una matriz vacía con la misma forma que x

# print(x)
# print()
# print(v)

# # Sumar el vector v a cada fila de la matriz x con un bucle explícito
# for i in range(4):
#     y[i, :] = x[i, :] + v

# print()
# print(y)

# x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# v = np.array([1, 0, 1])

# print(x)
# print()
# print(v)

# vv = np.tile(v, (4, 1))   # Amontonar 4 copias de V una encima de la otra
# print()
# print(vv)                 # Prints "[[1 0 1]
#                           #          [1 0 1]
#                           #          [1 0 1]
#                           #          [1 0 1]]"
# y = x + vv  # Agrega x y vv elementalmente
# print()
# print(y)