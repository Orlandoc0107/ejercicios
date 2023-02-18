from tkinter import *
# Entry = columna de textos

raiz=Tk()
miFrame=Frame(raiz, width=100, height=100)
miFrame.pack()

minombre=StringVar() # decile al cuadro nombre que estar asociado con esta variable

#--------------------------------
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textocomentario=Text(miFrame, width=16, height=5)
textocomentario.grid(row=4, column=1, padx=10, pady=10)

#Scrollbar barra de visora
scrollVert=Scrollbar(miFrame, command=textocomentario.yview)
scrollVert.grid(row=4, column=2, sticky="NSEW")
textocomentario.config(yscrollcommand=scrollVert.set)


nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky = "W", padx=10)

passLabel=Label(miFrame, text="Pass: ")
passLabel.grid(row=1, column=0, sticky = "W", padx=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0,sticky = "W", padx=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=3, column=0, sticky = "W", padx=10)

comentarioLabel=Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=4, column=0, sticky = "W", padx=10)


#Creacion de Botton

def codigoBoton():

    minombre.set("Variable_creada_solo es un ejemplo")


botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()


#------------------------------------
# sticky = N,ne E,es S,sw W nw (posicionamiento)
raiz.mainloop()
