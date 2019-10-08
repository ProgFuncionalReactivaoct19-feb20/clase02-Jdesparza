"""
	Ejemplo 6: uso de función Lambda
	Jdesparza
"""
# se crea una lista
lista = [10, 2, 3, 5, 1]
# print(min(lista, key=lambda x: x))
# print(min(lista, key=lambda x: x))
# variable que guarda el valor de x sumado 100
funciones = lambda x: x+100
# se imprime el valor minimo, haciendo uso de la operacion funciones
print(min(list(map(funciones, lista))))