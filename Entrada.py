# En este otro programa se mostrara en la ejecucion cuando un numero es entero o no, ya sea que lleva decimales.
# Primero se pedira que ingreses un numero para que el usuario lo pueda poner.
# Aparte de imprimir el numero que coloque el usuario pondra que tipo es, ya sea type o str.
entrada=input()
print(type(entrada))
# Aqui se volvera a usar el if, porque habra distintos resultados.
# En primer lugar, cuando coloques un numero entero te saldra la impresion que si es un dato entero, esto se observa en la linea 14.
# Y en segundo lugar, cuando coloques un numero que contenga decimales la impresion saldra que no es un dato entero, esto se muestra en la linea 17.
# Si el resultado es entero, este se contara como True.
# Y si el resultado no es entero, se contara como False.
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    # Lineas que se ejecutaran si la condicion es verdadera (True)
    print("Dato entero. ¡Muy bien!")
else:
    # Lineas que se ejecutaran si la condicion es falsa (False)
    print("Dato no es entero. Intentar nuevamente.")
