#En este segundo ejercicio, tendréis que crear un programa que tenga una #clase llamada Alumno que tenga como atributos su nombre y su nota. #Deberéis de definir los métodos para inicializar sus atributos, #imprimirlos y mostrar un mensaje con el resultado de la nota y si ha #aprobado o no.

class Alumno:
    def __init__(self):
        self.nombre = input ("Ingrese el nomcre del Alumno: ")
        self.nota = int(input ("Ingrese la nota del estudiante del 1 al 10: "))

    def aprovado(self):
        if self .nota >= 5:
            return ("esta Aprobado")
        else:
            return ("No Aprobo")

alumno = Alumno()
print (alumno.nombre + " " + alumno.aprovado())
