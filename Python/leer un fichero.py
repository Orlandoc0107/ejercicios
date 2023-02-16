#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.


#f = open('/home/orlando/documentos/ip.txt', 'r')
#r: lectura
#a: append --> ajuntar
#w: escritura
#x: crea

#t: texto
#b: binary

#datos = f.read()
#f.close()
#print(datos)
import os

directorio_inicio = os.path.expanduser("~")
ruta_archivo = os.path.join(directorio_inicio, "documentos" , "ip")

with open(ruta_archivo, 'r') as f:
    datos = f.read()

print(datos)
