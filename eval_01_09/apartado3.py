#autor: Juan Carlos Fernandez
#fecha: 01/09/2023
#Apartado 3 de la evalauacion continua

import tkinter as tk
import mysql.connector
from mysql.connector import Error

def busqueda():
# funcion que ejecuta la consulta a partir del valor introducido
# devuelve el resultado en el cuadro de texto

    input_programa = texto_entrada.get()

    comando = 'select country.name, city.name, city.district , city.countrycode from country, city where country.Capital = city.ID and country.name like "'+ input_programa +'"'
    cursor.execute(comando)
    datos = cursor.fetchall() # método que recoje la información devuelta por la consulta
    cuadro_texto.delete("1.0","end") # se borra el contenido del widget de texto cuando se ejecuta una nueva consulta
    for fila in datos: # se itera sobre la lista datos con el objeto fila
        cuadro_texto.insert(tk.END, fila) # Mostramos la salida en el widget de texto
        cuadro_texto.insert(tk.END, "\n") # Insertamos un salto de linea en el widget de texto
try:
    # Datos necesarios para establecer la conexión a la BBDD (IP, puerto, usuario, contraseña, base de datos)
    connection = mysql.connector.connect(
        host='212.227.153.120',
        port=3306,
        user='AFD_admin',
        password='Access_@pp694',
        db='world_x')
    
    if connection.is_connected():
        cursor = connection.cursor() # objeto "cursor" que ejecutará los métodos apropiados para la BBDD

        #### Definición de la GUI
        #  Ventana principal
        principal = tk.Tk()
        principal.title("Apartado 3 ***** Consulta BBDD*****")
        principal.geometry("600x400")
        
        #  Widget Frame
        marco = tk.Frame(principal)
        marco.grid(column=0, row=0, padx=(50,50), pady=(10, 10))
        marco.columnconfigure(0, weight=5)
        marco.rowconfigure(0, weight=3)

        # Widget Label
        etiqueta = tk.Label(marco, text="Coloca el nombre del País y te dire unas cosas: ")
        etiqueta.grid(column=2, row=1, sticky=(tk.W,tk.E))

        # Widget Entry (dato de entrada)
        valor = ""
        texto_entrada = tk.Entry(marco, width=20, textvariable=valor)
        texto_entrada.grid(column=3, row=1)

        # Widget Button
        boton = tk.Button(marco, text="Busqueda Rapida", command=busqueda)
        boton.grid(column=3, row=2, pady=(10,10))

        # Widget Text
        cuadro_texto = tk.Text(marco, height=15, width=60)
        cuadro_texto.grid(column=2, row=3, columnspan=4, pady=10)

    

        principal.mainloop()
        #### Final de la GUI

except Error as ex:
    print("Error durante la conexión: {}".format(ex)) # se informa en caso de error
    
finally:
    if connection.is_connected():
        connection.close()  # se cierra la conexión a la BD
        print("La conexión ha finalizado.")
    print("Fin del programa Amigo")
