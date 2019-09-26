# En este programa tendras que interactuar con el usuario pidiendole un valor.
# Cuando el usuario coloque un valor, se imprimira si es correcto o incorrecto dependiendo de como se ejecute el comando.
# Este programa tendran que ser numeros multiplos, y hasta contando el numero 0.
# Se captura un numero y se almacena una vez que es
# convertido a int
numero=int(input("Dame un numero entero: "))
# Se almacenan en valores booleanos la evaluacion
# de residuales. Si el residual es cero, quiere decir
# que el numero es multiplo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
# Cuando se usa and, se resuelve por verdadero si todas
# las condiciones son verdaderas. Cuando se usa or, se
# resuelve por verdadero si al menos una condicion es
# verdadera. Los parentesis le dicen a Python que
# las primeras dos condiciones son juntas, y la tercera
# es independiente.
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")
