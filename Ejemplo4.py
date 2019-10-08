"""
	Ejemplo 4: uso de función Lambda
	Jdesparza
"""
# Cada elemento de datos, tiene (edad y estatura)
# Se crea una dupla
datos = ((30, 1.79), (25, 1.60), (35, 1.68))
# variable para guardar  los valores de la posicion 2 de la dupla
dato = lambda x: x[2]
# variable para guardar el valor de la posicion 0
edad = lambda x: x[0]
# variable para guardar el valor de la posicion 1 multiplicado por 100
edad = lambda x: x[1]*100

# Se imprime el valor de la variable edad
print(edad(dato(datos)))