#Escribir un programa que calcule el precio promedio de un producto. El #precio promedio se
#debe calcular a partir del precio del mismo producto en tres #establecimientos distintos.

def promedios ():
    uno = float(input("Ingrese el valor del Primer producto: "))
    dos = float(input("Ingrese el valor del Segundo producto: "))
    tres = float(input("Ingrese el valor del Tercer producto: "))

    respuesta = round(((+dos+tres)/3),2)

    return print("El promedio del producto es de "+ str(respuesta) +" %")

