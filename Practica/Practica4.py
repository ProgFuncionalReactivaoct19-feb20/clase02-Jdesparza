"""
	Jdesparza
"""
import math
# se crea una lista
lista = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
# variable que guarda el valor dado elevado al cubo
operacion = lambda x: x**3
# se imprime la lista con los nuevos valores
print(list(map(operacion, lista)))
