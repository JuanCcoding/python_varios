import tkinter as tk

def mostrar():
    print("Nombre: %s \nApellido(s): %s \nCorreo Electronico: %s \nUbicación: %s \nMensaje: %s" % (e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))

def ejemplo_entrada():
    global e1, e2, e3, e4, e5  # Añadir global para que las entradas sean accesibles en la función mostrar

    principal = tk.Tk()
    principal.title ("Formulario de Contacto")

    tk.Label(principal, text="Nombre: ",
            padx = 20).grid(row=0)
        
    tk.Label(principal, text="Apellido(s): ",
            padx = 20).grid(row=1)

    tk.Label (principal,text="Correo Electronico" , padx=20).grid(row=2)

    tk.Label (principal,text="Ubicación" , padx=20).grid(row=3)

    tk.Label (principal,text="Mensaje" , padx=20).grid(row=4)
        
    e1 = tk.Entry(principal)
    e2 = tk.Entry(principal)
    e3 = tk.Entry(principal)
    e4 = tk.Entry(principal)
    e5 = tk.Entry(principal)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)  # Corregir la ubicación de e5
        

    tk.Button(principal, text="Enviar Mensaje",
        command=principal.destroy).grid(row=5, column=0, sticky=tk.W, pady=4)
    tk.Button(principal, text="Mostrar en consola",
        command=mostrar).grid(row=6, column=1, sticky=tk.W, pady=4)
                         
    principal.mainloop()

def main():
    ejemplo_entrada()

if __name__ == "__main__":
    main()
