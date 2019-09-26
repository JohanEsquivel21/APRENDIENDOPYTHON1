# En este programa sera un ciclo de sumas, ya que primero tendras que pedir al usuario que ponga y numero, y despues otro y este se ira sumando sin fin.
# En pocas palabras, sera un acumulado de numeros o mas bien, de puras sumas sin fin.
# Se declaran las variables de trabajo, con tipo explicito.
acumulado=int(0)
numero=str("")

# Al colocar True como condicion de while, esto hace que se formara un ciclo sin fin, osea que sera infinito la suma de los numeros.
# Y para romper este ciclo se tendra que usar el break para que de fin al ciclo.
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        # Si el numero es vacio, reporta la situacion y sale. Aqui sera donde se aplicara el break
        print("Vacio. Salida del programa.")
        break
    else:
        # Si se proporciono valor, acumulado = acumulado + numero
        # Se realiza el calculo usando suma incluyente (+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))
