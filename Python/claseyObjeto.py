#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color
#Ruedas
#Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad
#Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola


class vehiculo:
    def __init__(self):
        self.color = "color"
        self.ruedas = "ruedas"
        self.puertas = "puertas"


class coche(vehiculo):
    def __init__(self):
        super().__init__()
        self.velocidad = "velocidad"
        self.cilindrada = "cilindrada"


ferrari = coche()

print (ferrari.color)
print (ferrari.ruedas)
print (ferrari.puertas)
print (ferrari.velocidad)
print (ferrari.cilindrada)
