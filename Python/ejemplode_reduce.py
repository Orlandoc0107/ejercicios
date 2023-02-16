from functools import reduce

lista = [1, 2, 3, 4, 5]

def suma(a, b):
    return a + b

resultado = reduce(suma, lista)

print(resultado)
