import tkinter as tk

def mostrar_selecciones():
    # Recorrer las variables asociadas para mostrar su estado
    for i, var in enumerate(variables):
        print(f"Opción {i+1}: {'Seleccionada' if var.get() else 'No seleccionada'}")

# Crear ventana principal
window = tk.Tk()
window.title("Generar Checkbuttons con For")

# Lista de opciones
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5"]

# Crear una lista para guardar las variables asociadas a cada Checkbutton
variables = []

# Crear los Checkbuttons dinámicamente
for opcion in opciones:
    var = tk.BooleanVar()  # Variable para controlar el estado del checkbox
    variables.append(var)  # Guardar la variable en la lista
    tk.Checkbutton(window, text=opcion, variable=var).pack(anchor="w")

# Botón para mostrar las selecciones
tk.Button(window, text="Mostrar Selecciones", command=mostrar_selecciones).pack(pady=10)

window.mainloop()
