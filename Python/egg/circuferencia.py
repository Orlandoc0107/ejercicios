#Conocido el número en matemática PI π, pedir al usuario que ingrese el valor del radio de
#una circunferencia y calcular y mostrar por pantalla el área y perímetro. Recuerde que para
#calcular el área y el perímetro se utilizan las siguientes fórmulas:
#area = PI * radio2
#perimetro = 2 * PI * radio
import math
def circulo ():
    radio = float(input("Ingrese el valor de la radio : "))

    area = round((math.pi)*(radio**2),3)

    perimetro = round( 2*(math.pi)*radio, 3)

    print("El área de la circunferencia es " + str(area) + " y el perímetro es " + str(perimetro))


