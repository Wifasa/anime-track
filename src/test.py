import tkinter as tk

def eliminar_todos_los_labels():
    # Elimina todos los Label en la ventana
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

# Crear la ventana principal
window = tk.Tk()
window.title("Eliminar Todos los Labels")

# Crear Labels y un botón
for i in range(5):
    tk.Label(window, text=f"Label {i+1}").pack(pady=5)

tk.Button(window, text="Eliminar Todos los Labels", command=eliminar_todos_los_labels).pack(pady=20)

# Ejecutar la ventana
window.mainloop()
