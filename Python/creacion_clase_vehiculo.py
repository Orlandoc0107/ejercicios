#En este segundo ejercicio, tendréis que crear un archivo py y dentro #crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en #un archivo y luego lo cargamos.

import pickle

class Vehículo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

mi_coche = Vehículo("Toyota", "Corolla", 2021)

# Guardamos el objeto en un archivo
with open("mi_coche.pickle", "wb") as archivo:
    pickle.dump(mi_coche, archivo)

# Cargamos el objeto del archivo
with open("mi_coche.pickle", "rb") as archivo:
    objeto_cargado = pickle.load(archivo)

print(objeto_cargado)
