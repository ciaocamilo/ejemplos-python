# x=0
# x = x + 1
# print(x)

# y = 10
# y = y-1
# print(y)

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Despegue!')

# def factorial(n: int) -> int:
#     resultado = 1
#     numero_actual = 2
#     while numero_actual <= n:
#         resultado = resultado * numero_actual
#         numero_actual += 1
#         print(resultado)
#         print(numero_actual)
#     return resultado

# print(factorial(5))

# i = 1
# while i > 0:
#     print(i)
#     i = i+ 1
# print("Terminé")

# i = 1
# while i != 10:
#     print(i)
#     i = i+ 2
# print("Terminé")

# i = 'pedro'
# while i == 'pedro':
#     print(i)
#     i = input("nombre")
# print("Terminé") #aqui tambien le toca hacer lo mismo

# promedio, total, contar = 0.0, 0, 0

# print("Introduzca la nota de un estudiante (-1 para salir): ")
# grado = int(input())
# while grado != -1:
#     total = total + grado
#     contar = contar + 1
#     print("Introduzca la nota de un estudiante (-1 para salir): ")
#     grado = int(input())
# promedio = total / contar
# print("Promedio de notas del grado escolar es: " + str(promedio))

# variable = 10

# while variable > 0:
#     print('Actual valor de variable:', variable)
#     variable = variable -1
#     if variable == 5:
#         break
# print('salió')

# variable = 10

# while variable > 0:
#     variable = variable -1
#     if variable < 5:
#         continue
#     print('Actual valor de variable:', variable) # no imprime el 5

# a, b = 0, 1
# while b < 100:
#     print(b),
#     a, b = b, a + b

# for x in range(0, 10, 2):
#     print("Estamos en la iteración " + str(x))

# for j in range(10, 0, -1):
#     print("Estamos en la iteración " + str(j))

# oracion = 'Mary entiende muy bien Python'
# frases = oracion.split() # convierte a una lista cada palabra
# print("La oración analizada es:", oracion, ".\n")
# print(frases)
# print("\n")

# ['Mary', 'entiende', 'muy', 'bien', 'Python']

# for palabra in range(len(frases)):
#     print("Palabra: {0}, en la frase su posición es: {1}".format(
#         frases[palabra], palabra))

# datos_basicos = {
#     "nombres":"Leonardo Jose",
#     "apellidos":"Caballero Garcia",
#     "cedula":"26938401",
#     "fecha_nacimiento":"03/12/1980",
#     "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
#     "nacionalidad":"Venezolana",
#     "estado_civil":"Soltero"
# }
# # clave = datos_basicos.keys()
# # valor = datos_basicos.values()

# cantidad_datos = datos_basicos.items()

# # print(clave)
# # print(valor)
# # print(cantidad_datos)

# for clave, valor in cantidad_datos:
#     print(clave + ": " + valor)

# frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}

# for nombre, color in frutas.items():
#     print(nombre, "es de color", color)

# db_connection = "127.0.0.1","5432","root","nomina"

# for parametro in db_connection:
#     print(parametro)

# print("""El comando PostgreSQL es:
# $ psql -h {server} -p {port} -U {user} -d {db_name}""".format(
# server=db_connection[0], port=db_connection[1],
# user=db_connection[2], db_name=db_connection[3]))