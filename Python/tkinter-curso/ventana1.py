#Raiz (tk) ventana
# Elementos Frame
# dentro de Frame widgets , hasta un Frame se consider un widgets.
from tkinter import *
raiz = Tk()
#le podemos dar un titulo a la ventana
raiz.title("Ventana de pruebas")
# resizable es para inmovilizar la ventana
#    raiz.resizable(0,0)
#primer 0 ancho, width , segundo 0 largo
# para conocar un incono ("ruta ") no funciona
#raiz.iconbitmap('archlinux.ico')
# tamano por defecto
#raiz.geometry("650x350")
# color de fondo
raiz.config(bg="black")
#podemos agregarle bodes ala raiz
raiz.config(relief="sunken")
raiz.config(bd=5)
# creacion de Frame
miFrame=Frame()
miFrame.pack() # para redimencional el Frame podemos posicionalo escribiendo dentro de los ( ) 'left', 'right', 'top', 'bottom'
# otra opcion si redimencionamos es usando (fill="y") , si queremos que se expanda usaremos (expand="True")
# color de Frame
miFrame.config(bg="red")
# redimencion de Frame
miFrame.config(width='350', height="125")
#bode de la ventana
miFrame.config(bd=5)
#efectos del borde
miFrame.config(relief="sunken")
# curso del raton
miFrame.config(cursor="hand2")
raiz.mainloop()
