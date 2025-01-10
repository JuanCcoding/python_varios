import tkinter as tk

root = tk.Tk()

framesNum = 160
archivo = "logo.gif"

# Lista de todas las imágenes del gif
frames = [tk.PhotoImage(file=archivo, format='gif -index %i' % i) for i in range(framesNum)]

def update(ind):
    """ Actualiza la imagen gif """
    frame = frames[ind]
    ind += 1
    if ind == framesNum:
        ind = 0
    canvas.create_image(0, 0, image=frame, anchor=tk.NW)
    root.after(20, update, ind) # Numero que regula la velocidad del gif

canvas = tk.Canvas(root, width=300, height=100) # Modificar segun el tamaño de la imagen

canvas.pack()
root.after(0, update, 0)
root.mainloop()
