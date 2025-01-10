#autor: Juan Carlos Fernandez
#fecha: 01/09/2023
#Apartado 1 de la evaluacion continua


import tkinter as tk

# En este modulo obtenemos los datos del Entry necesarios para hacer los calculos
def calculo_hipoteca ():



    f_capital_inicial= float (capital.get())
    f_interes=float (interes.get())
    i_cuotas_anuales= int(cuotas_anuales.get())
    i_cantidad_años= float (años.get())


    total_cuotas= i_cuotas_anuales * i_cantidad_años
    
    factor =(1+f_interes*0.01/i_cuotas_anuales)**total_cuotas
    print (factor)
    total_pagar=factor*f_capital_inicial
    importe_cuotas=total_pagar/total_cuotas
   
    #aninados los siguientes elementos .config a cada una de las etiquetas que estaban vacias y que queremos mostrar por pantalla
    
    resultado1.config(text=f"{total_cuotas:.0f}")
    resultado2.config(text=f"{total_pagar:.2f} Euros")
    resultado3.config(text=f"{importe_cuotas:.2f}")


def datos():

    global capital
    global interes
    global cuotas_anuales
    global años
    global resultado1
    global resultado2
    global resultado3


    principal = tk.Tk()
    principal.title ("Càlculo de Hipotecas Juan el rapido")
    principal.geometry ("400x200")

    tk.Label(principal, text="Capital Inicial: ",padx = 20).grid(row=0)
        
    tk.Label(principal, text="Tasa de Interes (TAE): ",padx = 20).grid(row=1)

    tk.Label (principal,text="Numero de cuotas anuales:" , padx=20).grid(row=2)

    tk.Label (principal,text="Numero de años:" , padx=20).grid(row=3)

    resultado1=tk.Label (principal,text="Total de cuotas:" , padx=20).grid(row=6)
    resultado2=tk.Label (principal,text="Total a pagar:" , padx=20).grid(row=7)
    resultado3=tk.Label (principal,text="Importe mensual de cada cuota:" , padx=20).grid(row=8)


    valor1=""
    valor2=""
   # Valor3=""
    valor4=""
    
    capital= tk.Entry(principal,textvariable=valor1)
    interes= tk.Entry(principal,textvariable=valor2)
    cuotas_anuales= tk.Entry(principal)
    
    años= tk.Entry(principal,textvariable=valor4)

    resultado1= tk.Label(principal)
    resultado2= tk.Label(principal)
    resultado3= tk.Label(principal)
    

    capital.grid(row=0, column=1)
    interes.grid(row=1, column=1)
    cuotas_anuales.grid(row=2, column=1)
    años.grid(row=3, column=1)

    #resultado del total de cuotas
    resultado1.grid(row=6, column=1)
    #resultado del total a pagar
    resultado2.grid(row=7, column=1)
    #resultado del importe mensual de cada cuota
    resultado3.grid(row=8, column=1)
    

    tk.Button(principal, text="Calcular Hipoteca", command=calculo_hipoteca).grid(row=10, column=0, sticky=tk.W, pady=4)                 
    principal.mainloop()

datos ()

