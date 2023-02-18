#tkinter
#WxPython
#PyQt
#PyGtK
#--------------------------
#from tkinter import *
import tkinter
# creando una ventana  , de clase TK ,  usar T mayuscula
ventana = tkinter.Tk()

# print(type(ventana)) #muestra el tipo
# import pprint
# pprint.pprint(dir(ventana))
#-----------------------------

# tipo de posesamientos:
#1

label_saludo = tkinter.Label(ventana, text='Hola', bg='yellow', fg='blue')
label_saludo.pack(ipadx=59, ipady=58, fill='both', expand=True)
#fill puede ser y ,x o both # side='left' , side='right'

label_adios = tkinter.Label(ventana, text='adios', bg='red', fg='white')
label_adios.pack(ipadx=59, ipady=100, fill='both')

# se debe general un loop para mantener la ventana abierta
ventana.mainloop()

