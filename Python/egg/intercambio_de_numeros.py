#Escriba un programa que permita al usuario ingresar el valor de dos variables numéricas de
#tipo entero. Posteriormente, el programa debe intercambiar los valores de ambas variables
#y mostrar el resultado final por pantalla.
#Por ejemplo, si el usuario ingresa los valores num1 = 9 y num2 = 3, la salida a del
#programa deberá mostrar: num1 = 3 y num2 = 9
#Ayuda: Para intercambiar los valores de dos variables se debe utilizar una variable auxiliar.

def intercambiar():
    num1 = int(input("Ingrese un primer numero: "))
    num2 = int(input("Ingrese un segundo numero: "))

    print("el primer numero es :" + str(num1))

    print("el segundo numero es :" + str(num2))

    aux = num1
    num1 = num2
    num2 = aux

    print("------------------------")

    print("Ahora el primer numero es " + str(num1) + " El segundo numero es " + str(num2))
