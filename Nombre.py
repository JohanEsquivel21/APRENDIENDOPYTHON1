# En este programa lo que se va a ejecutar o correr es que tu puedas poner tu nombre y apellido, podremos interactuar como usuario.
# Cuando se ejecute todo este programa, nosotros tenemos que almacenar o escribir los datos cuando se ejecuta.
# Nos dara la opcion de poder poner nuestros nombre y nuestro apellido, y este se imprimira en mayusculas.

nombre=input("Nombre:")
apellidos=input("Apellidos:")
# Primero se escribiran los valores str(string, ya que solo se utilizaran puras letras), junto con las comillas " ".
nombreCompleto=nombre+" "+apellidos
# Despues se utilizara un comando para que lo que este escrito se ejecute todo en mayusculas.
nombreCompleto=nombreCompleto.upper()
print(nombreCompleto)
