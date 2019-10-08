"""
	Jdesparza
"""
# para importar las operaciones matematicas
import math
# se crea unlistado con duplas
datos = [(10, 2), (8, 7), (5, 4), (3, 11), (10, 11)]
# variable para recorrer los valores de la posicion 0 en las duplas
raizcuadrada = lambda x: x[0]
# variable para recorrer los valores de la posicion 1 en las duplas
potencia = lambda x: x[1]
# variable con las operaciones para las variables raizcuadrada, potencia
operacion = lambda x: (math.sqrt(raizcuadrada(x)), math.pow(potencia(x),2))
# se imprime el listado con las nuevas duplas
print(list(map(operacion, datos)))