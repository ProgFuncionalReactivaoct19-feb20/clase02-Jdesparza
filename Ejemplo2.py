"""
	Ejemplo 2: uso de función Lambda
	Jdesparza
"""
# Se crea una lista con variables enteras
lista = [10, 2, 3, 5]
# Variable para guardar  el valor de la posicion 2
mifuncion = lambda x: x[2]
# Se imprime la variable mifuncion
print(mifuncion(lista))