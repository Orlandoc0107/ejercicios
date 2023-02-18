import tkinter
from tkinter import ttk

ventana =tkinter.Tk()

var1=2
var2=3
var3=var1+var2

label1 = tkinter.Label(ventana, text="la suma de los numero es igual a " + str(var3) , bg='blue', fg='white')
label1.place(x=10, y=50)

ventana.mainloop()
