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
	
	definir num Como Real
	Definir i,j,x como entero
	
	Dimension vector(2)
	escribir "Ingrese el numero a Evaluar"
	leer num
	
	i=0
	j=0
	Para i<-1 Hasta num  Hacer
		si num%i=0 Entonces
			j=j+1
		FinSi
	Fin Para
	
	si j=2 Entonces
		escribir" El numero es primo"
	SiNo
		escribir "No es un numero primo"
	FinSi
	
FinAlgoritmo