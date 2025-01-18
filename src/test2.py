import tkinter as tk

def mostrar_seleccion():
    print(f"Opción seleccionada: {opcion_seleccionada.get()}")

# Crear la ventana principal
window = tk.Tk()
window.title("Checkbuttons Exclusivos")

# Variable que controla qué checkbutton está marcado
opcion_seleccionada = tk.StringVar(value="")  # Valor inicial vacío

# Crear los Checkbuttons
tk.Checkbutton(
    window, 
    text="Opción 1", 
    variable=opcion_seleccionada, 
    onvalue="Opción 1", 
    offvalue="").pack(anchor="w")

tk.Checkbutton(
    window, 
    text="Opción 2", 
    variable=opcion_seleccionada, 
    onvalue="Opción 2", 
    offvalue="").pack(anchor="w")

tk.Checkbutton(
    window, 
    text="Opción 3", 
    variable=opcion_seleccionada, 
    onvalue="Opción 3", 
    offvalue="").pack(anchor="w")

# Botón para mostrar la selección actual
tk.Button(window, text="Mostrar Selección", command=mostrar_seleccion).pack(pady=10)

window.mainloop()
