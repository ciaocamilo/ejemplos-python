def comprarRopa(nino:str, mujer: str, hombre: str, tarjeta_puntos:bool) ->dict:
# def total(nino:str, mujer: str):
    # Crear el diccionario con los valores de entrada
    prendas = {
        'nino':{'Camiseta' : 19900, 'Saco': 45000},
        'mujer' :{'Vestido' : 60000, 'Camiseta manga corta': 35000},
        'hombre' : {'Chaqueta' : 90000, 'Camisa': 59500},
        'tarjeta_puntos':{'Sí posee la tarjeta' : True, 'No posee la tarjeta': False}
    }
    # Se crea un diccionario con los datos de entrada, para compararlos entre sí
    compras =  {
        'niño': nino,
        'mujer' : mujer,
        'hombre' : hombre,
        'bono': 0,
        'total': int(0)
    }
    # Se esta calculando el total llamando el diccionario de prendas y agregando el total al diccionario de compras
    # Que las prendas que compré existan en el diccionario llamado
    if compras['niño'] in prendas['nino']:
        compras['total'] +=  prendas['nino'][compras['niño']]
    if compras['mujer'] in prendas['mujer']:
        compras['total'] +=  prendas['mujer'][compras['mujer']]
    if compras['hombre'] in prendas['hombre']:
        compras['total'] +=  prendas['hombre'][compras['hombre']]
    # Total de las entradas
    # Condicional para calcular el bono
    if (tarjeta_puntos == True) or (mujer == 'Vestido' and hombre == 'Chaqueta') :
        compras['bono'] = 0.5
        compras['total'] -= int(compras['total'] * 0.15)
    return compras


print(comprarRopa('Camiseta', '', 'Camisa', False))
print(comprarRopa('Saco', 'Vestido', 'Camisa', True))
print(comprarRopa('Saco', 'Vestido', 'Chaqueta', False))
print(comprarRopa('', 'Camiseta manga corta', '', True))