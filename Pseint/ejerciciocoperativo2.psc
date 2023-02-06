Algoritmo sin_titulo
Escribir "_________________________________________________________________________________________"	
escribir "|#######                                                    ###     #     ###   ####### |" 
escribir "|#     # #####  #        ##   #    # #####   ####   ####   #   #   ##    #   #  #    #  |"  
escribir "|#     # #    # #       #  #  ##   # #    # #    # #    # #     # # #   #     #     #   |"   
escribir "|#     # #    # #      #    # # #  # #    # #    # #      #     #   #   #     #    #    |"    
escribir "|#     # #####  #      ###### #  # # #    # #    # #      #     #   #   #     #   #     |"     
escribir "|#     # #   #  #      #    # #   ## #    # #    # #    #  #   #    #    #   #    #     |"     
escribir "|####### #    # ###### #    # #    # #####   ####   ####    ###   #####   ###     #     |"
Escribir "|_______________________________________________________________________________________|"
escribir " "
escribir "Bienvenidos a mi codigo"
escribir " "
Esperar 3 Segundos
escribir "3"
esperar 1 Segundos
escribir "2"
esperar 1 Segundos
escribir "1"
esperar 1 Segundos
Borrar Pantalla
//////////////////////////
///ingresar usuario y contrasena
///

definir usuario,contrasena Como Caracter
definir intentos,menu como entero
definir login Como Logico
menu=0
///usuario="orlando"
///contrasena="123"
Login=Falso

escribir "Ingrese Su Usuario"
leer usuario

Mientras usuario<>"orlando" Hacer
	escribir "ingrese su usuario"
	leer usuario
Fin Mientras

intentos=0

si usuario="orlando" Entonces
	
	Mientras intentos<>3 Hacer
		
		escribir "Ingrese su contrasena"
		leer contrasena
		
		intentos=intentos+1
		
		Si contrasena="123" Entonces
			login=Verdadero
			intentos=3
		SiNo
			escribir "Contrasena incorrecta ,porfavor intenta de nuevo"
			escribir "Intento numero --> " intentos
		Fin Si
		
	Fin Mientras
	Borrar Pantalla
	Si login=Verdadero Entonces
		escribir "Ingresando al Login ...Cargando el sistema"
		esperar 2 Segundos
		menu=1
		Borrar Pantalla
	SiNo
		escribir "se finalizo tus intentos"
		escribir "Fin del Programa"
	Fin Si
	///////////
	
	Borrar Pantalla
	definir opciones Como Caracter
	definir botellas Como real
	definir saldo como real
	definir peso como real
	definir i Como Real
	definir gramos como real
	definir respuesta Como Caracter
	
	saldo=0
	Repetir
		escribir "Ingresando al Menu"
		escribir "Ingrese (1) si desea , Ingresar la cantidad de botellas"
		escribir "Ingrese (2) si desea , Consultar saldo"
		escribir "Ingrese (3) si desea , Salir del Programa"
		
		leer opciones
		Segun opciones Hacer
			
			"1":
				escribir "Ingresar Botellas"
				escribir "Cuantas botellas desea ingresar al sistema?"
				leer botellas
				/////
				peso=0
				para i=1 Hasta botellas Hacer
					esperar 1 Segundos
					escribir "calculando las botellas numero " i
					escribir " "
					gramos=Aleatorio(100,3000)
					escribir "Calculando el peso de las botellas " gramos " gr" 
					escribir " "
					Peso=peso+gramos
				FinPara
				escribir "Limpiando la pantalla"
				esperar 1 Segundos
				Borrar Pantalla
				
				si peso<500 Entonces
					saldo=50
				FinSi
				si peso>=501 y peso <= 1500 Entonces
					saldo=125
				FinSi
				si peso>1501 Entonces
					saldo=200
				FinSi
				
				/////
				escribir "Calculando el Saldo espere uno segundos "
				escribir "se le ofrece un valor de " saldo " $"
				escribir "desea aceptarlos ?  ingrese (s) si desea aceptalos o una (n) si no lo desea "
				leer respuesta
				
				si respuesta="S" o respuesta="s" Entonces
					Escribir "lo acreditamosa su saldo"
				FinSi
				
				si respuesta="n" o respuesta="N" Entonces
					escribir "Devolviendo Material"
					esperar 2 Segundos
					saldo=0
				FinSi
				
				esperar 2 Segundos
			"2":
				escribir "consultar saldos"
				escribir "Su saldo es un total de " saldo "$"
				esperar 2 segundos
				saldo=0
			"3":
				escribir "Cerrando el Sistema"
				login=Falso
				Esperar 2 Segundos
		FinSegun
		Borrar Pantalla
		Esperar 1 Segundos
	Mientras Que login=Verdadero
	
	escribir "Gracias por usar el Programa"
	
FinSi


FinAlgoritmo
