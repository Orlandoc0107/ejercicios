#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

numero = [ ]

i=1-1
while i<100:
    i=i+1
    numero.append(i)
    rev = list (reversed(numero))


print(rev)


