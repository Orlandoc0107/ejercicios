#Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

entrada = input("Introduce una lista de países separados por comas: ")
lista_paises = [pais.strip().lower().capitalize() for pais in entrada.split(',')]
set_paises = set(lista_paises)
lista_ordenada = sorted(set_paises)
cadena_paises = ", ".join(lista_ordenada)
print(cadena_paises)
