# En este programa mas que todo no podras interactuar como usuario, ya que la impresion te saldra lo que hayas escrito como maquina.
# Aqui se mostraran las tablas numericas del 1 al 10.
# Primero escribiras que las tablas que vayan a poner esten entre un rango de 1 al 11.
for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    # print sin argumentos es un salto de linea.
    print()
    # Dentro de un for, se pone otro for, viene siendo algo parecido con el if.
    for j in range(1,11):
        # Aqui, i contiene el numero base de la tabla, tipo el numero por el cual se va a multiplicar.
        # Y la j sera el numero el cual es el multiplicador de la base.
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        # Al final se ejecutara el codigo, el que viene siendo un salto de linea.
        print()
