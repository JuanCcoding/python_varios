import tkinter as tk
#import * 
import random
import string

def generar_pass():
    pass_longitud = int(longitud.get())
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation)
    for _ in range(pass_longitud))
    resultado_pass.delete(0, tk.END)
    resultado_pass.insert(0, password)

def index():
    global longitud  # Declarar la variable longitud como global
    global resultado_pass
    principal = tk.Tk()
    principal.title("PASSWORD GENERATOR By Juancarlos Fernandez")
    principal.geometry("700x200")

#creamos nuestro primer widget de salida tipo "Label"
    tk.Label(principal, text="Indica la longitud de caracteres para tu contraseña:").grid(row=0, columnspan=2, padx=20, pady=10)

#creamos un widget de tipo "Entry"
    longitud = tk.Entry(principal)
    longitud.grid(row=0, column=2, padx=10)

#creamos nuestro segundo widget de salida tipo "Label"
    tk.Label(principal, text="Tu contraseña generada es:").grid(row=1, columnspan=2, padx=20, pady=10)

#creamos un widget de tipo "Entry"
    resultado_pass = tk.Entry(principal,width=40)
    resultado_pass.grid(row=1, column=2, padx=10)


#creamos 2 botones

 # boton que llama al modulo generar_pass y me genera la contraseña

    boton1 = tk.Button(principal, text="Generar", bg='blue',command=generar_pass)
    boton1.grid(row=2, columnspan=3, pady=10)

# boton que llama al comando 'quit' y me cierre el programa
    boton2 = tk.Button(principal, text="Cerrar Programa", command=quit)
    boton2.grid(row=4, columnspan=4, pady=20)

    principal.mainloop()

index()






