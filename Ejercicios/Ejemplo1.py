"""
	Ejemplo 1: uso de función Lambda
	Jdesparza
"""
# Creación de una lista con variables de tipo entero
lista = [10, 2, 3, 5]
# Se imprime el valor minimo haciendo el uso de lambda
print(min(lista, key=lambda l: l))
# print(min(lista, key=lambda x: x+100))
