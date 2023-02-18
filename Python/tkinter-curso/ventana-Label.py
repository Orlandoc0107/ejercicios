# Wigets
# Label
from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miLabel= Label(miFrame, text="Hola , Soy un Ejemplo Python", fg="blue" , font=("hack ", 18))
miLabel.pack()
#metodo miLabel.place(x=100, y=200)

# la libreria trabaja con imagenes

miImagen=PhotoImage(file="archlinux.png")

root.mainloop()
