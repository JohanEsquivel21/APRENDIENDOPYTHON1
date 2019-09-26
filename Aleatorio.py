# En el lenguaje Python, se utilizan muchos comandos. Tambien existen las librerias.
# En las librerias existen los modulos, y los modulos son por asi decirlo comandos ya hechos, practicamente te facilita la realizacion de hacer comandos.
# Y para poder utilizar un modulo, primero debe importarse, y para importarse se utiliza el comando import.
import random

# Despues se define una variable tipo float, y se le va a asignar un valor cualquiera.
numero1=float(10.5)

# En este programa basicamente haremos que el valor que nosotros estamos utilizando en el float, se le sume un numero aleatorio.
# Y a continuacion se mostrara el comando de como se suma el valor float con el numero random o aleatorio.
# Despues utilizaremos el comando def. Este comando hace que todo lo que esta escrito que se ve mas a la derecha forme parte de la funcion.
# En resumen, se almacenara todo lo escrito con el comando def.
def miFuncion():
    # Aqui se convertita a float el numero o valor aleatorio que se genero por el comando random.randrange().
    # Este comando solamente se podra ejecutar si se importa el numero aleatorio o random.
    numero2=float(random.randrange(1,10))
    # A continuacion utilizaremos meta sustituciones para poder ver los resultados.
    mensaje="La suma de {} y {} es {}"
    # Y por ultimo imprimiremos el resultado de los numeros que se van a sumar (el float y el numero random).
    print(mensaje.format(numero1,numero2,numero1+numero2))

# Y ya al final, se ejecutara la funcion definida en el codigo.
miFuncion()
