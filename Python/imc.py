#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en una carpeta comprimida zip.

import math

peso = float(input('Ingrese su peso en K: '))
altura = float(input("Ingrese su altura en metros: "))

imc = round(peso/math.pow(altura,2),2)

print ("Tu indice de masa corporal es "+ str(imc))
