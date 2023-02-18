#tkinter
#WxPython
#PyQt
#PyGtK
#--------------------------
#from tkinter import *
import tkinter
from tkinter import ttk
# creando una ventana  , de clase TK ,  usar T mayuscula
ventana = tkinter.Tk()
#(0,0) (1,0) (2,0)
#(0,1) (1,1) (2,1)
#(0,2) (1,2) (2,2)

############################

# label #Entry
# label #Entry #button

############################
# ejemplo de una input box
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

username_label = ttk.Label(ventana, text="Username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
#padx ancho ... pady alto
#stiky (posicion rosa de los vientos en ingles W)

username_entry = ttk.Entry(ventana) #entrada de texto
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5) #ubicacion de la columna
#-----------------------
#contrasena

password_label = ttk.Label(ventana, text="password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)
#padx ancho ... pady alto
#stiky (posicion rosa de los vientos en ingles W)

password_entry = ttk.Entry(ventana, show='*') #entrada de texto
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5) #ubicacion de la columna

# para ocultar la contrasena, usamos password_entry = ttk.Entry(ventana, show='x')
# se debe general un loop para mantener la ventana abierta

#--------------

#botom

login_button = ttk.Button(ventana, text="login")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)


ventana.mainloop()
