#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

#Al principio no tiene que haber una opción seleccionada.

import tkinter
from tkinter import ttk

lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

ventana = tkinter.Tk()

seleccion = IntVar()

#

Radiobutton(ventana, text="Opcion 1", variable=seleccion, value=1).pack()

Radiobutton(ventana, text="Opcion 2", variable=seleccion, value=2).pack()

Button(ventana, text="Verificar", command=lambda: verificar(seleccion.get())).pack()

def verificar(opcion):
    if opcion == 1:
        print("Has seleccionado la opcion 1")

ventana.mainloop()
