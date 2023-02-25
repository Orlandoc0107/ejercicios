#Checkbutton

# botones de seleccion para respuestas multiples

from tkinter import *

root=Tk()

root.title("Ejemplo")

## variables creadas

playa=IntVar()
montaxa=IntVar()
turismoRural=IntVar()

def opcionesViaje():

    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+=" playa"

    if(montaxa.get()==1):
        opcionEscogida+=" montaxa"

    if(turismoRural.get()==1):
        opcionEscogida+=" turismoRural"

    textoFinal.config(text=opcionEscogida)

## ---------------------

foto=PhotoImage(file="avion.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destino", width=50).pack()


Checkbutton(root, text="playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="montaxa", variable=montaxa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()
