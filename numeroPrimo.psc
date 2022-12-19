Algoritmo sin_titulo
	
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