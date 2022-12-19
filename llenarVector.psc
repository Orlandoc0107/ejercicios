Algoritmo sin_titulo
	
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
