import tkinter as tk


def calculo ():

    nota1= float (e3.get())
    nota2= float (e4.get())
    nombre= e1.get()
    dni=e2.get()


    if nota1 >10 or nota1<0:
        print ("Advertencia: Valores encontrados fuera del rango  0-10")
    if nota2 >10 or nota2<0:
        print ("Advertencia: Valores encontrados fuera del rango 0-10")
    
    notafinal= 0.3* nota1 + 0.7 * nota2
    #salida = tk.Label (principal,text=notafinal , padx=60).grid(row=4)
    resultado.config(text=f"{notafinal:.2f}")

    notafinal_str= str(notafinal)
    notas_alumnos= "notas_alumnos.txt"
    datos_a_guardar = f"{nombre} {dni} {nota1} {nota2} {notafinal_str}\n"

    # Leer el contenido existente del archivo
    try:
        with open(notas_alumnos, 'r') as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        lineas = []

    # Sobrescribir solo los datos del alumno con el mismo nombre
    with open(notas_alumnos, 'w') as archivo:
        for linea in lineas:
            if linea.startswith(nombre):
                archivo.write(datos_a_guardar)
            else:
                archivo.write(linea)
        if not any(linea.startswith(nombre) for linea in lineas):
            archivo.write(datos_a_guardar)

    print("Datos guardados exitosamente en", notas_alumnos)

def datos():

    global e1
    global e2
    global e3
    global e4
    global resultado


    principal = tk.Tk()
    principal.title ("Expediente Notas del Curso")

    tk.Label(principal, text="Nombre: ",padx = 20).grid(row=0)
        
    tk.Label(principal, text="DNI: ",padx = 20).grid(row=1)

    tk.Label (principal,text="Nota obtenida en la evaluación continua:" , padx=20).grid(row=2)

    tk.Label (principal,text="Nota obtenida en la evaluación final:" , padx=20).grid(row=3)

    resultado=tk.Label (principal,text="Nota definitiva:" , padx=20).grid(row=4)


    valor1=""
    valor2=""
    e1 = tk.Entry(principal)
    e2 = tk.Entry(principal)
    e3 = tk.Entry(principal, textvariable=valor1)
    e4 = tk.Entry(principal,textvariable=valor2)
    resultado= tk.Label(principal)
    

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    resultado.grid(row=4, column=1)
    

    tk.Button(principal, text="Calcular Nota", command=calculo).grid(row=5, column=0, sticky=tk.W, pady=4)                 
    principal.mainloop()

datos ()
