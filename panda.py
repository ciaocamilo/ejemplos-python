import pandas as pd
import numpy as np

# ventas = pd.Series([15,12,21], index = ["Ene", "Feb", "Mar"])
# # print(ventas)
# # print(ventas[0])
# # print(ventas["Mar"])

# # print(ventas.dtype)

# ventas.name = "Ventas 2020"
# ventas.index.name = "Meses"

# # print(ventas.index)
# # print(ventas.values)
# # print(ventas.name)
# print(ventas)

# # print(ventas.axes)

# print(ventas.shape)

# datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }

# compras = pd.DataFrame( datos , index = [ 'Juno' , 'Robert' , 'Lily' , 'David' ])

# # compras = pd.DataFrame( datos )
# print(compras)

# print(compras.index)
# print(compras.columns)

# print(compras.axes)

# s = pd.Series([7,5,3])
# s = pd.Series([7,5,3], index = ["Ene", "Feb", "Mar"])

# d = {"Ene":7, "Feb":5, "Mar":3 }
# # s = pd.Series(d)
# # s = pd.Series(d, index = ["Abr", "Mar", "Feb", "Ene"],dtype=int)

# s = pd.Series(7, index = ["Ene", "Feb", "Mar"])

# print(s)

# elementos = {
#     "Numero atómico":[1, 6, 47, 88],
#     "Masa atómica":[1.008, 12.011, 107.87, 226],
#     "Familia":["No metal", "No metal", "Metal", "Metal"]
# }

# # tabla_periodica = pd.DataFrame(elementos)
# tabla_periodica = pd.DataFrame(elementos,
#                                index = ["H", "C", "Ag", "Ra"],
#                                columns = ["Familia", "Numero atómico", "Masa atómica"]
# )


# print(tabla_periodica)

# unidades_Datos = np.array([[2, 5, 3, 2],
#                          [4, 6, 7, 2],
#                           [3, 2, 4, 1]])
# # print(unidades_Datos)

# # unidades = pd.DataFrame(unidades_Datos)
# unidades = pd.DataFrame(unidades_Datos, index = [2015, 2016, 2017], columns = ["Ag", "Au", "Cu", "Pt"])
# print(unidades)

# unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2}
# unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
# unidades_2017 = {"Ag":3, "Au":2, "Cu":4, "Pt":1}

# unidades = pd.DataFrame([unidades_2015, unidades_2016, unidades_2017],
#                        index = [2015, 2016, 2017])
# print(unidades)

# unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2}
# unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
# unidades_2017 = {"Ag":3, "Pb":2, "Cu":4, "Pt":1}

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

# # print(almacén)

# print(entradas.head())
# print(almacén.head())

# entradas.tail()
# almacén.tail()

# print(entradas.sample())
# print(almacén.sample(5))

# print(almacén.describe())

# print(almacén.info())

# import numpy as np
# s = pd.Series([3, 1, 2, 1, 1, 4, 1, 2, np.nan])

# print(s.value_counts())

# print(s.value_counts(dropna = False))
# print(s)

# print(s.value_counts(bins = 2))

# s = pd.Series([10, 20, 30, 40])

# print(s[0])
# print(s[2])

# s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])

# print(s["a"],s[0])
# print(s["d"],s[3])

# s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])

# print(s[1:3])

# s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
# print(s)
# print()
# print(s["b":"d"])

# s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
# print(s)
# print()
# print(s.iloc[1])
# print(s.iloc[0])
# print(s.iloc[3])

# print(s.iloc[-1])
# print(s.iloc[-4])
# print(s.iloc[1:-1])

# s = pd.Series([5, 2, -3, 7, 8, 4])
# print(s[s>2])
# print(s[[True, False, False, True, True, False]])
# print(s.iloc[(s>2).values])

# s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "s"])
# # print(s.sample(2, random_state = 7))

# # print(s.sample(frac = 0.6, random_state = 18))
# print(s.sample(10, random_state = 18, replace = True))

# s = pd.Series([1, 2, 3, 4])
# print(s)
# print()
# s.pop(1)
# print(s)

# s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
# print(s)
# print()
# print(s.pop("a"))
# print()
# print(s)

# ventas = pd.DataFrame({
#     "Entradas":[41, 32, 56, 18],
#     "Salidas":[17, 54, 6, 78],
#     "Valoración": [66, 54, 49, 66],
#     "Límite": ["No", "Si", "No", "No"],
#     "Cambio": [1.43, 1.16, -0.67, 0.77]},
#     index = ["Ene", "Feb", "Mar", "Abr"])
# print(ventas)
# print()

# # print(ventas["Entradas"])
# # print(ventas["Entradas"]["Feb"])

# ventas["Entradas"] = [33, 25, 40, 12]
# ventas["Salidas"]=1

# # ventas["Pérdidas"] = pd.Series([5, 4, 6, 8], index = ["Ene", "Mar", "Abr", "May"])

# ventas["Ganancias"] = (ventas["Entradas"]*2) - (ventas["Valoración"]/10)

# print(ventas)
# print()
# print(ventas.Ganancias)

# df = pd.DataFrame(np.arange(18).reshape([6, 3]),
#                   index = ["a", "b", "c", "d", "d", "f"],
#                   columns = ["A", "B", "C"])
# print(df)
# print()
# print(df["b":"d"])

# print(df[:3])
# print(df[:"c"])

# print(df.get("A"))
# print()
# print(df.get("D"))

# df = pd.DataFrame(np.arange(18).reshape([6, 3]),
#                   index = ["a", "b", "c", "d", "e", "f"],
#                   columns = ["A", "B", "C"])


# print(df.loc["b":"d"])

# print(df.loc[["e", "c"], "B"])

# df = pd.DataFrame(np.random.randint(0, 10, 18).reshape([6, 3]),
#                index = ["a", "b", "c", "d", "e", "f"],
#                columns = ["A", "B", "C"])

# df = pd.DataFrame(np.arange(18).reshape([6, 3]),
#                  index = ["a", "b", "c", "d", "e", "f"],
#                  columns = ["A", "B", "C"])
# df



# print(df.columns.get_loc("B"))
# print(df.columns.get_indexer(["A", "C"]))

# print(df.index.get_loc("d"))
# print(df.index.get_indexer(["c", "e"]))

# df = pd.DataFrame(np.arange(18).reshape([6, 3]),
#                  index = ["a", "b", "c", "d", "e", "f"],
#                  columns = ["A", "B", "C"])
# print(df)
# print()
# mask = [True, False, True, False, False, True]
# print(mask)
# print()
# print(df[mask])
# print(df[df.A > 7])
# print(df.iloc[(df.B > 6 ).values])

# df = pd.DataFrame(np.arange(18).reshape([6, 3]),
#                   index = ["a", "b", "c", "d", "e", "f"],
#                   columns = ["A", "B", "C"])

# print(df)
# print()
# # print(df.sample(3, random_state = 18))
# # print(df.sample(2, random_state = 18, axis = 0))
# # print(df.sample(frac = 0.6, random_state = 18))

# columna = df.pop("B")
# print(columna)
# print()
# print(df)

# s = pd.Series([1, 2, 3, 4, 5], index = ["a", "b", "c", "d", "e"])
# print(s)
# print()
# # s[1:3] = 0
# # s["b":"d"] = -2
# # s[1:3] = [0, 1]
# # s["b":"d"] = [10, 11, 12]
# # s["f"] = 0
# # s["f":"h"] = 0
# # s[["c", "a"]] = [1, 2]
# # s[[1, 0]] = [20, 21]
# print()
# # r = s.drop("b")
# r = s.drop(["d", "a"])
# print(r)

# s = pd.Series(np.arange(0, 10))
# print(s)
# print()
# print(s.where(s % 2 == 0, -1))

# df = pd.DataFrame(np.arange(12).reshape(-1, 3), columns=["A", "B", "C"])
# print(df)
# print()
# print(df.where(df % 2 == 0, -df))

# df = pd.DataFrame(np.arange(16).reshape([4, 4]),
#                   index = ["a", "b", "c", "d"],
#                   columns = ["A", "B", "C", "D"])
# print(df)
# print()
# print(df.drop(columns = ["B", "D"]))

# s = pd.Series([1, 2, 3, 4, 5,], index = ["a", "b", "c", "d", "e"])
# r = pd.Series([10, 11, 12], index = ["f", "g", "h"])

# a = pd.Series([1, 2, 3, 4, 5,], index = ["a", "b", "c", "d", "e"])
# b = pd.Series([10, 11, 12], index = ["a", "b", "f"])

# print(a)
# print()
# print(b)
# print()
# print(pd.concat([a, b], axis = 1, sort = True))

# s = pd.Series([1, 2, 3, 4], index = ["a", "b", "c", "d"])
# r = pd.Series([10, 11, 12], index = ["a", "c", "e"])
# print(pd.concat([s, r], axis = 1))

# a = pd.Series([1, 2, 3, 4, 5], index = ["a", "b", "c", "d", "e"])
# b = pd.Series([10, 11, 12], index = ["f", "g", "h"])
# # c = a.append(b)
# c = a.append(b, ignore_index = True)
# print(c)

# df1 = pd.DataFrame(np.arange(9).reshape([3, 3]),
#                   index = ["a", "b", "d"],
#                   columns = ["A", "B", "C"])
# print(df1)
# print()
# df2 = pd.DataFrame(np.arange(12).reshape([4, 3]),
#                   index = ["a", "b", "c", "e"],
#                   columns = ["B", "C", "D"])
# print(df2)
# print()

# print(pd.concat([df1, df2], axis = 0, join = "inner", ignore_index = True))

df1 = pd.DataFrame(np.arange(9).reshape([3, 3]),
                  index = ["a", "b", "d"],
                  columns = ["A", "B", "C"])
print(df1)
print()
df2 = pd.DataFrame(np.arange(12).reshape([4, 3]),
                  index = ["a", "b", "c", "e"],
                  columns = ["B", "C", "D"])
print(df2)
print()

print(df1.append(df2, sort = False))