from numpy.core.fromnumeric import ravel
import pandas as pd
import numpy as np

# ventas = pd.Series([15,12,21], index = ["Ene", "Feb", "Mar"])
# # print(ventas)
# # print(ventas['Feb'])
# # print(ventas.values)

# ventas.name = "Ventas 2020"
# ventas.index.name = "Meses"
# print(ventas.shape)

# datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }
# compras = pd.DataFrame( datos , index = [ 'Juno' , 'Robert' , 'Lily' , 'David' ])
# compras.index.name = "Clientes"
# compras.columns.name = "Frutas"
# # compras = pd.DataFrame( datos )
# print(compras.shape)

# d = {"Ene":7, "Feb":5, "Mar":3 }
# # s = pd.Series(d, index = ["Abr", "Mar", "Feb", "Ene"], dtype=int)
# s = pd.Series(7, index = ["Ene", "Feb", "Mar"])
# print(s)

##############################################################################
# elementos = {
#     "Numero atómico":[1, 6, 47, 88],
#     "Masa atómica":[1.008, 12.011, 107.87, 226],
#     "Familia":["No metal", "No metal", "Metal", "Metal"]
# }

# tabla_periodica = pd.DataFrame(elementos,
#                                index = ["H", "C", "Ag", "Ra"],
#                                columns = ["Familia", "Numero atómico", "Masa atómica"]
# )
# tabla_periodica.index.name = 'Elementos'
# # tabla_periodica = pd.DataFrame(elementos)
# print(tabla_periodica)

#############################################

# unidades_Datos = np.array([[2, 5, 3, 2],
#                          [4, 6, 7, 2],
#                           [3, 2, 4, 1]])

# unidades = pd.DataFrame(unidades_Datos, index = [2015, 2016, 2017], columns = ["Ag", "Au", "Cu", "Pt"])
# unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2}
# unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
# unidades_2017 = {"Ag":3, "Au":2, "Cu":4, "Pt":1}

# unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2}
# unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
# unidades_2017 = {"Ag":3, "Pb":2, "Cu":4, "Pt":1}

# unidades = pd.DataFrame([unidades_2015, unidades_2016, unidades_2017],
#                        index = [2015, 2016, 2017])

# unidades = pd.DataFrame([unidades_2015, unidades_2016, unidades_2017],
#                        index = [2015, 2016, 2017])
# print(unidades)

# entradas = pd.Series([11, 18, 12, 16, 9, 16, 22, 28, 31, 29, 30, 12],
#             index = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago",
#              "sep", "oct", "nov", "dic"])
# print(entradas)
# print()
# salidas = pd.Series([9, 26, 18, 15, 6, 22, 19, 25, 34, 22, 21, 14],
#             index = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago",
#              "sep", "oct", "nov", "dic"])
# print(salidas)
# print()
# almacén = pd.DataFrame({"entradas": entradas, "salidas": salidas})

# almacén["neto"] = almacén.entradas - almacén.salidas

# print(almacén)
# print()

# # print(entradas.tail())
# # print()
# # print(almacén.tail())

# # print(almacén.sample(6))
# print(almacén.describe())
# almacén.info()

# s = pd.Series([3, 1, 2, 1, 1, 4, 1, 2, np.nan])
# print(s)
# print(s.value_counts(bins = 3))

# s = pd.Series([5, 2, -3, 7, 8, 4])
# print(s.iloc[(s>2).values])

# s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "s"])
# print(s.sample(10, random_state = 18, replace = True))

# s = pd.Series([1, 2, 3, 4])
# try:
#     s.pop(1)
#     print(s)
# except:
#     print("Error")

# ventas = pd.DataFrame({
#     "Entradas":[41, 32, 56, 18, np.nan],
#     "Salidas":[17, 54, 6, 78, np.nan],
#     "Valoración": [66, 54, 49, 66, np.nan],
#     "Límite": ["No", "Si", "No", "No", np.nan],
#     "Cambio": [1.43, 1.16, -0.67, 0.77, np.nan]},
#     index = ["Ene", "Feb", "Mar", "Abr", "May"])

# ventas["Entradas"] = [33, 25, 40, 12, np.nan]
# ventas["Pérdidas"] = pd.Series([5, 4, 6, 8], index = ["Ene", "Mar", "Abr", "May"])
# ventas["Ganancias"] = (ventas["Entradas"]*2) - (ventas["Valoración"]/10)
# print(ventas.Ganancias)

# df = pd.DataFrame(np.arange(18).reshape([6, 3]),
#                   index = ["a", "b", "c", "d", "e", "f"],
#                   columns = ["A", "B", "C"])
# print(df)
# print()
# # print(df.loc[["e", "c"], "B"])
# print(df.index.get_indexer(["c", "e"]))

# df = pd.DataFrame(np.arange(18).reshape([6, 3]),
#                  index = ["a", "b", "c", "d", "e", "f"],
#                  columns = ["A", "B", "C"])
# print(df)
# print()
# # mask = [True, False, True, False, False, True]
# print(df[df.A > 7])

# df = pd.DataFrame(np.arange(18).reshape([6, 3]),
#                   index = ["a", "b", "c", "d", "e", "f"],
#                   columns = ["A", "B", "C"])

# print(df.sample(frac = 0.6, random_state = 18))

# s = pd.Series(np.arange(0, 10))
# print(s.where(s % 2 == 0, -s))

# df = pd.DataFrame(np.arange(12).reshape(-1, 3), columns=["A", "B", "C"])
# print(df)
# print()
# print(df.where(df % 2 == 0, -df))

# df = pd.DataFrame(np.arange(16).reshape([4, 4]),
#                   index = ["a", "b", "c", "d"],
#                   columns = ["A", "B", "C", "D"])

# print(df.drop(["B", "D"], axis = 1))

# s = pd.Series([1, 2, 3, 4, 5,], index = ["a", "b", "c", "d", "e"])
# r = pd.Series([10, 11, 12], index = ["f", "g", "h"])


# t = pd.concat([s, r])
# print(t)

# a = pd.Series([1, 2, 3, 4, 5,], index = ["a", "b", "c", "d", "e"])
# b = pd.Series([10, 11, 12], index = ["a", "b", "f"])
# print(pd.concat([a, b], axis = 1, sort = True))

# a = pd.Series([1, 2, 3, 4, 5], index = ["a", "b", "c", "d", "e"])
# b = pd.Series([10, 11, 12], index = ["f", "g", "h"])

# print(a.append(b, ignore_index = True))

df1 = pd.DataFrame(np.arange(9).reshape([3, 3]),
                  index = ["a", "b", "d"],
                  columns = ["A", "B", "C"])
print(df1)
print()
df2 = pd.DataFrame(np.arange(12).reshape([4, 3]),
                  index = ["a", "b", "c", "e"],
                  columns = ["B", "C", "D"])
# print(df2)
# print()
# print(pd.concat([df1, df2], axis = 1, join = "inner"))

print(df1.append(df2, sort = False))
