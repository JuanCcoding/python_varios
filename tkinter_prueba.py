import tkinter as tk

def ejemplo_label ():

    principal = tk.Tk()
    principal.title ("Ejemplo introducir imagen y texto label")
    logo = tk.PhotoImage (file="anillo.gif")
    texto = input ("Indicame que necesitas frodo:  ")
    w1 = tk.Label (principal,image =logo).pack (side="right")
    w2 = tk.Label (principal,text =texto).pack (side="left")
    principal.mainloop()

def ejemplo_mensaje ():
    principal = tk.Tk()
    principal.title ("Ejemplo boton mensaje")
    texto =""" Hola mundo maravilloso siempre habra motivos para sonreir"""
    msg= tk.Message (principal, text = texto)
    msg.config(bg='lightblue', font=('times', 14))
    msg.pack()
    principal.mainloop()

def escribir_slogan ():
    print ("Bienvenuti a mi slogan")

def descanso ():
    print ("Vaaaaaaaamossssss")
    
def ejemplo_button ():
    principal = tk.Tk()
    principal.title ("Ejemplo de boton simple")
    fotograma = tk.Frame (principal)
    fotograma.pack ()

    boton_salir = tk.Button (fotograma, text ="Curioso,Pincha aqui", fg="red", command=quit)
    boton_salir.pack(side=tk.LEFT)
    
    boton_slogan = tk.Button(fotograma,text="Hola", command=escribir_slogan)
    boton_slogan.pack(side=tk.RIGHT)

    boton_descanso = tk.Button(fotograma,text="Es hora del receso", command=descanso)
    boton_descanso.pack(side=tk.RIGHT)
    principal.mainloop()

def ejemplo_radiobutton():
    principal = tk.Tk()
    principal.title ("Ejemplo de Radio Boton")
    V= tk.IntVar()

    tk.Label(principal, text = "Elija un lenguaje de programacion",
             justify = tk.LEFT,
             padx = 20).pack()

    tk.Radiobutton(principal, text="Python",
        padx=20,
        variable = V,
        value=1).pack (anchor=tk.W)

    tk.Radiobutton(principal, text="C++",
        padx=20,
        variable = V,
        value=2).pack (anchor=tk.W)

    tk.Radiobutton(principal, text="Java",
        padx=20,
        variable = V,
        value=3).pack (anchor=tk.W)

    principal.mainloop()

def ejemplo_checkbutton():

    principal = tk.Tk()
    principal.title ("Ejemplo check boton")

    v1= tk.IntVar()
    
    tk.Checkbutton(principal, text = "Male",
        padx=20,
        variable = v1).grid (row=0,sticky=tk.W)

    v2= tk.IntVar()
    
    tk.Checkbutton(principal, text = "Female",
        padx=20,
        variable = v2).grid (row=1,sticky=tk.W)


    principal.mainloop()

def ejemplo_entrada():

    def mostrar():
        print("Titulo: %s \nAutor(s): %s \nOtros Datos: %s \nUbicación: %s" % (e1.get(), e2.get(),e3.get(), e4.get()))

    principal = tk.Tk()
    principal.title ("Archivo de libros")

    tk.Label(principal, text="Titulo: ",
        padx = 20).grid(row=0)
    
    tk.Label(principal, text="Autor(s): ",
        padx = 20).grid(row=1)

    tk.Label (principal,text="Otros Datos" , padx=20).grid(row=2)

    tk.Label (principal,text="Ubicación" , padx=20).grid(row=3)
    
    e1 = tk.Entry(principal)
    e2 = tk.Entry(principal)
    e3 = tk.Entry(principal)
    e4 = tk.Entry(principal)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    

    tk.Button(principal, text="Salir",
        command=principal.destroy).grid(row=4, column=0, sticky=tk.W, pady=4)
    tk.Button(principal, text="Mostrar en consola",
        command=mostrar).grid(row=4, column=1, sticky=tk.W, pady=4)
                     
    principal.mainloop()



def ejemplo_barra():

    principal= tk.Tk()
    principal.title("Ejemplo de widget scroll bar")
    S=tk.Scrollbar(principal)
    T= tk.Text(principal, height=4, width=50)
    S.pack(side=tk.RIGHT, fill = tk.Y)
    T.pack(side=tk.LEFT, fill = tk.Y)
    principal.geometry("125x100")
    S.config(command=T.yview)
    T.config (yscrollcommand=S.set)
    quote= """ HOLAAAAAAAAAAAAAAA
            cada vezzzzzzzzzzzz
            holaaaaaaaaaaaaaaaaa
            otra vezzzzzzz"""
    T.insert (tk.END,quote)
    principal.mainloop()
    

    

def main ():
    while True:
        
        print ("Benvido a mi programa basico de eleccion de widgets con tkinter")
        opcion = input ("Pulsa la Letra A, B , C ,D , E  , F o G y pasaran cosas:  ")
        if opcion == "A":
            ejemplo_label ()
        elif opcion == "B":
            ejemplo_mensaje()
        elif opcion == "C":
            ejemplo_button()
        elif opcion == "D":
            ejemplo_radiobutton()
        elif opcion == "E":
            ejemplo_checkbutton()
        elif opcion == "F":
            ejemplo_entrada()
        elif opcion == "G":
            ejemplo_barra()
        else:
            print ("opcion incorrecta")
            break


    print("Progama Terminado")

if __name__ == "__main__":
    main()
