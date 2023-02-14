import os

print ("Hola Este es un Menu de los ejercicios de Egg Version Python ")


print ("menu principal Porfavor, seleccione una de las opciones ")

guia = input( " Selecciones una Guia , Dispone 1,: ")
os.system ('clear')
if guia == "1":
    ejercicio = input(" Seleccione un Ejercicio, 1 , 2, 3, 4, 5: ")
    if ejercicio == "1":
        print ("Calculo de Area y Perimetro de una Circuferencia")
        input ("Presione una Tecla para continuar")
        import circuferencia
        import math
        #from circuferencia import circulo
        #from circuferencia import *
        circuferencia.circulo()

    if ejercicio =="2":
        print("promedio de un producto")
        input("Presione una Tecla para continuar")
        os.system ('clear')
        import promedio
        promedio.promedios()

    if ejercicio =="3":
        print("conversion en metros en centimetros, milimetros y pulgadas")

        input("Presione una Tecla para continuar")
        os.system ('clear')
        import metros
        metros.convertidor()

    if ejercicio =="4":
        print ("Consumo de combustible")
        os.system ('clear')
        import calculo_combustible
        calculo_combustible.calculo_combustible()

    if ejercicio =="5":
        print ("intercambio de numero")
        os.system('clear')
        import intercambio_de_numeros
        intercambio_de_numeros.intercambiar()

    else:
        print ("Hasta Luego")

else:
    print (" Hasta Luego")



print ("Gracias por usar el programa")
