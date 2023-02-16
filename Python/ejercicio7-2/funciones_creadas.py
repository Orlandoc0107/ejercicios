#En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

#Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.

respuesta = 0
print("Bienvenido, a la calculadora Basica")
a = float(input("Ingrese la primera cifra: "))
print("Que desea hacer con esa cifra ?")
print ("1 -) Sumar ")
print ("2 -) Restar ")
print ("3 -) Multiplicar ")
print ("4 -) Dividir ")

opcion = int(input("Ingrese el numero de la operacion que desee realizar: "))

b = float(input("Ingrese la segunda cifra: "))

if opcion == 1:
    import operaciones_basicas
    operaciones_basicas.suma(a, b)

if opcion == 2:
    import operaciones_basicas
    operaciones_basicas.restar(a, b)

if opcion == 3:
    import operaciones_basicas
    operaciones_basicas.multiplicar(a, b)

if opcion == 4:
    import operaciones_basicas
    operaciones_basicas.dividir(a, b)

else:
    print ("Opcion invalida intente nuevamente ,Gracias")
