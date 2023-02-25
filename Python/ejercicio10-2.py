#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

#Al principio no tiene que haber una opción seleccionada.


import tkinter as tk
import tkinter as IntVar

# creamos una ventana

ventana = tk.Tk()

#
variable_opciones = tk.IntVar()
# creamos una funcion

def seleccionado():
    if variable_opciones.get()==1:
        mostrar.config(text="Selecionaste Uno")
    if variable_opciones.get()==2:
        mostrar.config(text="Selecionaste Dos")
    if variable_opciones.get()==3:
        mostrar.config(text="Selecionaste Tres")
    if variable_opciones.get()==4:
        mostrar.config(text="Selecionaste Cuatro")
    if variable_opciones.get()==5:
        mostrar.config(text="Selecionaste Cinco")
    if variable_opciones.get()==6:
        mostrar.config(text="Selecionaste Seis")

def reinicia():
    mostrar.config(text="")

# creamos un mensaje en la partesuperior

mensaje = tk.Label(ventana, text="Seleccionada un numero:")
mensaje.pack()

# creamos un botones
uno = tk.Radiobutton(ventana, text="Uno", variable=variable_opciones, value=1, command=seleccionado)
uno.pack()
# creamos un botones
dos = tk.Radiobutton(ventana, text="Dos", variable=variable_opciones, value=2, command=seleccionado)
dos.pack()
# creamos un botones
tres = tk.Radiobutton(ventana, text="Tres", variable=variable_opciones, value=3, command=seleccionado)
tres.pack()
# creamos un botones
cuatro = tk.Radiobutton(ventana, text="Cuatro", variable=variable_opciones, value=4, command=seleccionado)
cuatro.pack()
# creamos un botones
cinco = tk.Radiobutton(ventana, text="Cinco", variable=variable_opciones, value=5, command=seleccionado)
cinco.pack()
# creamos un botones
seis = tk.Radiobutton(ventana, text="Seis", variable=variable_opciones, value=6, command=seleccionado)
seis.pack()
#
reinicio = tk.Button(ventana, text="Reiniciar", command=reinicia)
reinicio.pack()

mostrar=tk.Label(ventana)
mostrar.pack()

ventana.mainloop()
