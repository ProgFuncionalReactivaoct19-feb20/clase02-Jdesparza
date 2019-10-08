"""
	Jdesparza
"""
# se pide una valor por teclado
n = input("Ingrese un numero: \n")
# se transforma el valor en entero
n = int(n)
# se hace la operacion para determinar si es par
valor_par = lambda x: x%2 == 0
# se guarda en una variable la operacion realizada
valor = valor_par(n)
# se imprime si el valor es par
print(valor)
