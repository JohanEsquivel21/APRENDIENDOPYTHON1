# En este programa se compararan dos numeros, en los cuales se mostrara cual es el mayor y cual es el menor.
# Primero lo que se pide es que inserte los dos numeros, osea que le pidas al usuario dos numeros cualquiera.
# Aqui igualmente utilizaremos las meta sustituciones, mas bien, las llaves para poder almacenar dos numeros ahi y el resultado.
numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    # Aqui en esta impresion saldra que si pones los numeros son iguales pues te lo marcara.
    print(salida.format(numero1, numero2,"Los numeros son iguales"))
else:
    # Condicionales anidadas, if dentro de otro if. Esto es que hay otros resultados dentro de un resultado.
    # Si se llega a suceder de que los numeros no son iguales se abriria otro if con otros posibles resultados o impresiones.
    if numero1>numero2:
        # Aqui se imprimira o ejecutara si el primer numero es mayor al segundo.
        print(salida.format(numero1, numero2,"El mayor es el primero"))
    else:
        # Y aqui seria lo contrario, si el primero no es mayor al segundo.
        print(salida.format(numero1, numero2,"El mayor es el segundo"))
