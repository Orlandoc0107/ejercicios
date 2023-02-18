from tkinter import *

ventana = Tk()

ventana.title("Ejemplo de RadioButton")

ventana.geometry("400x200")

#creamos una variable de tipo entero

seleccion = IntVar()

#creamos los radiobutton

Radiobutton(ventana, text="Opcion 1", variable=seleccion, value=1).pack()

Radiobutton(ventana, text="Opcion 2", variable=seleccion, value=2).pack()

Radiobutton(ventana, text="Opcion 3", variable=seleccion, value=3).pack()

#creamos un boton para verificar la opcion seleccionada

Button(ventana, text="Verificar", command=lambda: verificar(seleccion.get())).pack()

ventana.mainloop()

#funcion para verificar la opcion seleccionada

def verificar(opcion):
    if opcion == 1:
        print("Has seleccionado la opcion 1")

    elif opcion == 2:
        print("Has seleccionado la opcion 2")
    else:
        print("Has seleccionado la opcion 3")
