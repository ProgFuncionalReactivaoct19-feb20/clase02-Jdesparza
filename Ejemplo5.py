"""
	Ejemplo 5: uso de función Lambda
	Jdesparza
"""
# se crea una dupla
datos = (
		(100, 170),
		(200, 180),
		)
# variable que guarda los valores en la posicion 0 de la dupla
anios = lambda x: x[0]
# Variable que guarda los valores de la posicion 1 de la dupla
estatura = lambda x: x[1]
# variable de operacion para las variables anios, estatura
funciones = lambda x: (anios(x)/12.0, estatura(x)/100)
# se imprimen los valores
print(list(map(funciones, datos)))