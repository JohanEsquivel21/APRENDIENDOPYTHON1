# En este programa lo que se va a imprimir o ejecutar seran las tablas numericas.
# Primero vas a tener que pedirle al usuario que escriba un numero cualquiera, en este caso, tiene que ser del 1 al 9.
# En la linea 5 convertiremos la variable en entero.
numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)
# A continuacion utilizaremos el comando for, la funcion de este comando es que ejecutara un bloque de codigo un numero determinado de veces, en un rango de 1-11.
# Esto del rango hace que los numero que tomara tendran que ser del 1 al 10.
# Despues se colocara que salida y se pondran las {} donde se colocaran los numeros que se van a multiplicar y tambien la del resultado de la operacion.
for i in range(1,11):
    # i va variando a cada iteracion.
    salida="{} x {} = {}"
    # Y por ultimo se imprimira el comando que hara que el numero que de el usuario se multiplique mediante la tabla numerica del numero que se inserto.
    print(salida.format(numero,i,i*numero))
