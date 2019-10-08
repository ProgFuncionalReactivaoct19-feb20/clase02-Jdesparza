"""
	Ejemplo 3: uso de función Lambda
	Jdesparza
"""
# Cada elemento de datos, tiene (edad y estatura)
# Se crea una dupla
datos = ((30, 1.79), (25, 1.60), (35, 1.68))
# variable para guardar  los valores de la posicion 2 de la dupla
dato = lambda x: x[2]
# Se imprime la variable dato
print(dato(datos))