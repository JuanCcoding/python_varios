from tkinter import *

principal= Tk()
entrada=Entry (principal,width=100)
principal.title ("Generador de contraseñas")
entrada.insert (0,"Escribe aqui tu super clave secreta")
entrada.grid(row=0, column=0)

def clic ():
    texto=Label(principal , text="Pruebame", padx=100)
    boton1 = Button(principal, text="Pruebame2", bg="blue",padx=100,pady=25,command=clic).grid(row=2,column=0)
    principal.mainloop ()
