# import numpy as np

# participantes = [[2,3,4], [4,1,7]]
# ajustados = []

# for part in participantes:
#     part = list(map(lambda puntaje: 3 if puntaje < 4 else puntaje, part))
#     ajustados.append(part)

# print(ajustados)


# matriz = np.array(ajustados)
# promedio = round(matriz.mean(), 2)
# calificacion = np.sum(matriz, axis = 1)
# ganador = calificacion.argmax() + 1

# import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/encuesta_chololates.csv', sep=';')

# # print(df)

# precios = df.groupby(['PRECIO']).size()

# print(type(df['PRECIO'].value_counts()))
# print(df['PRECIO'].value_counts().idxmax())
# print(df['PRECIO'].value_counts().max())

# print(precios)

# data["PRECIO"].value_counts()


import requests
r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=AAPL&resolution=1&from=1615298999&to=1615302599&token=')
print(r.json())