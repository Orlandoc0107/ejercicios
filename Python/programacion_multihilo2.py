#--------------------

#import logging , se usa para mensajes

#import logging
#logging.info("Arrancando programa")
#logging.warning("Hace Calor")

#---------

# funciones tipo Built-in

#filter , se crea o crear una lamda
numeros = [1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    if x % 2 == 0:
        return True

    return False

# si la funcion da true , filter mantendra el numero
# si la funcion da False , filter eliminara el numero
resultado = filter(mifuncion, numeros)
print (list(resultado))

# este programa hace un filtro de impares

resultado2 = filter(lambda x: x%2 != 0 , numeros)

print (list(resultado2))

print ("-----------")
#--------- funcion map

def cuadrado(x):
    return x * x

resultado3 = map(cuadrado,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(resultado3))



resultado4 = map(lambda x: x*x,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(resultado4))

print ("----------")
#------------- reduce

from functools import reduce

def suma(a, b):
    print (f' a={a}, b={b}')
    return a + b
print (" ")
res = reduce(suma, [1, 2, 3, 4, 5])
print( res)


print ("------------")
#-------------- zip

cursos = ['Java', 'Python', 'Git']
asistentes = [15, 20, 4]
demo = zip(cursos,asistentes)
print (list(demo))

#---------------

print("---------------")


#---------------- all

listaA= [1==2, 2==2, 3==4]
res1 = any(listaA)
print (res1) # devuelve True ya que una es cierta.
print ("--")
res2= all(listaA) # devuelve False obliga que toda sea cierta
print(res2)


print("----------------")

#-------------------

print (min(2, 3, 4, 5, 6, 7, 10))

print (pow(2, 4))

#-------------------ordenar lista o tuplas

lista10 = ['z', 'c', 'd', 'a']
ordenada = sorted(lista10)
print (ordenada)

#--------------------

print ("---------------------")

from getpass import getpass

user = input("Como te llamas?: ")
passwd = getpass("passwd: ")
print(user, passwd)

#---------- convertir un numero a stri

secreto = 50

valor = input("Introduce un numero: ")
valor = int(valor)


