#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

# Creamos el archivo de texto
archivo = open("ejemplo.txt", "w")

# Escribimos en el archivo
archivo.write("Hola Mundo \n")
archivo.write("Este deberia ser lasegunda linea \n")

# Cerramos el archivo
archivo.close()

# Abrimos el archivo de nuevo en modo lectura
archivo = open("ejemplo.txt", "r")

# Leemos el contenido del archivo
contenido = archivo.read()
print(contenido)

# Cerramos el archivo nuevamente
archivo.close()

