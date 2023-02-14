#A partir de una conocida cantidad de metros que el usuario ingresa a #través del teclado se
#debe obtener su equivalente en centímetros, en milímetros y en pulgadas.

def convertidor ():
    metros = float(input("Ingrese la cantidad de metro al  convertir : "))

    centimetros = round((metros*100),2)

    milimetros = round((metros*1000),2)

    pulgadas = round((metros*2.54),2)

    return print(str(metros) + " metros , tienen " + str(centimetros) + " cm , " + str(milimetros) + " ml y " + str(pulgadas) + " pulgadas")



