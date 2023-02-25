#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter as tk

ventana = tk.Tk()

etiqueta1 = tk.Label(ventana, text="Seleccione los elementos que desee")
etiqueta1.pack()

elementos_1 = tk.Checkbutton(ventana, text="Primer Elemento").pack()

elementos_2 = tk.Checkbutton(ventana, text="Segundo Elemento").pack()

elementos_3 = tk.Checkbutton(ventana, text="Tercer Elemento").pack()

elementos_4 = tk.Checkbutton(ventana, text="Cuarto Elemento").pack()

elementos_5 = tk.Checkbutton(ventana, text="Quinto Elemento").pack()

ventana.mainloop()
