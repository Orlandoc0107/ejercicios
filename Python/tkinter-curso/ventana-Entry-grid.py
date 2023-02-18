from tkinter import *
# Entry = columna de textos

raiz=Tk()
miFrame=Frame(raiz, width=100, height=100)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky = "W", padx=10)


apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0,sticky = "W", padx=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=3, column=0, sticky = "W", padx=10)

passLabel=Label(miFrame, text="Pass: ")
passLabel.grid(row=1, column=0, sticky = "W", padx=10)

# sticky = N,ne E,es S,sw W nw
raiz.mainloop()
