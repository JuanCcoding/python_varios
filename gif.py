import tkinter as tk

root = tk.Tk()

archivo = "logo.gif"

# Obtener el número de frames del gif
frames = []
i = 0
while True:
    try:
        frame = tk.PhotoImage(file=archivo, format=f'gif -index {i}')
        frames.append(frame)
        i += 1
    except tk.TclError:
        break

framesNum = len(frames)
running = True  # Variable para controlar el estado de la animación

def update(ind):
    """ Actualiza la imagen gif """
    if running:
        frame = frames[ind]
        ind += 1
        if ind == framesNum:
            ind = 0
        canvas.create_image(0, 0, image=frame, anchor=tk.NW)
        root.after(20, update, ind) # Numero que regula la velocidad del gif

def toggle_animation(event):
    """ Detiene o reanuda la animación al hacer clic """
    global running
    running = not running
    if running:
        update(0)

canvas = tk.Canvas(root, width=frames[0].width(), height=frames[0].height()) # Ajustar el tamaño del canvas al tamaño de la imagen
canvas.pack()

# Mantener una referencia a la imagen para evitar que sea recolectada por el garbage collector
canvas.image = frames[0]

canvas.bind("<Button-1>", toggle_animation)  # Vincular el clic del ratón a la función toggle_animation

root.after(0, update, 0)
root.mainloop()
