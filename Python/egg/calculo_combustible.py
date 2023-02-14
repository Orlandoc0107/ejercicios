#Escribir un programa que calcule cuántos litros de combustible consumió #un automóvil. El
#usuario ingresará una cantidad de litros de combustible cargados en la #estación y una
#cantidad de kilómetros recorridos, después, el programa calculará el #consumo (km/lt) y se
#lo mostrará al usuario.


def calculo_combustible():

    litros = float(input("Ingrese la cantidad de Litros Cargados: "))

    kilometros = float(input("Ingrese cuantos kilometros viajo el Vehivulo: "))

    consumo = round((kilometros / litros ),2)

    return print ("El consumo total de litro de combustible es de " + str(consumo) + " Litros ")
