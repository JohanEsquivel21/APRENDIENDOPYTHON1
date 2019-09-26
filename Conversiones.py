# A continuacion se declara una variable str(string), la variable str viene siendo puras letras, ya que asi se basa ese comando
numero= "1234"
# Despues de esto se muestra el tipo de variable que se esta utilizando.
# Despues en la salida se convierte a tipo type, en el tipo type se utilizan numeros y en esta ocasion lo necesitaremos.
print(type(numero))
# A continuacion, ahora se convertira a tipo int.
numero=int(numero)
# Aqui vemos que esto cambia al utilizar diferente comando, pero la variable seguira haciendo por asi decirlo la misma funcion, mas bien, no cambia.
print(type(numero))
# Luego, se declarara una variable str con meta sustitucion, aqui es donde iran seleccionados los valores que se utilizaron, usando format.
salida="El numero utilizado es {}"
# Al ultimo se mostrara la impresion o resultado cuando lo corres. La funcion de la meta sustitucion hara que el valor de los numeros se coloque entre las {}
print(salida.format(numero))
