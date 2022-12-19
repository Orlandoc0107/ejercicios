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
	
	definir vector,num,i Como Entero
	
	Escribir "Ingrese la dimension del Vector"
	leer num
	Dimension vector(num)
	
	para i=0 Hasta num-1 Hacer
		 
		escribir "Ingrese el valor del vector " i
		leer vector(i)
		
	FinPara
	Borrar Pantalla
	
	para i=0 Hasta num-1 Hacer
		escribir Sin Saltar "[" vector(i) "] " 
	FinPara
	
FinAlgoritmo
