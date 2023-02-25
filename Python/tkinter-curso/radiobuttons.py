from tkinter import *

root=Tk()

# el nombre de la ventana es root

varOpcion=IntVar()

def imprimir():
	#print(varOpcion.get())
	if varOpcion.get()==1:
		etiqueta.config(text="Has elegido Masculino")

	elif varOpcion.get()==2:
		etiqueta.config(text="Has elegido Femenino")

	else:
		etiqueta.config(text="Has elegido otros")



Label(root, text="Genero:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

Radiobutton(root, text="Otras Opciones", variable=varOpcion, value=3, command=imprimir).pack()

#en ves de impirmiren a consola se imprime en la intefaz

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()
