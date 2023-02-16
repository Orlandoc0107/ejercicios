#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.


from functools import reduce


lista = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (lista)
print ("Elimanando los numeros impares")
print (" ")
def impar (x):
    if x % 2 == 0:
        return False

    return True
impares = filter(impar, lista)
impares2 = filter(impar,lista)
reducir = (list(impares))
print (list(impares2))
print (" ")
print ("Sumando los numeros impares ")
print (" ")
#

from functools import reduce

def suma(a, b):
    return a + b

resultado = reduce(suma, reducir)

print(resultado)
