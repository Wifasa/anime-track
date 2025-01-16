import tkinter as tk

class Windows_tk:

    def __init__(self,window):
        self.window = window

    def window_main_menu(self):
        self.window.title("Main menu")

        self.window.geometry("400x250+600+600")

        tk.Label(self.window, text="Add New Amime:").grid(row=0, column=0,sticky="nsew")
        tk.Button(self.window, text="Select", borderwidth=1, relief="solid", command=lambda: self.update_new()).grid(row=0, column=1,sticky="nsew")

        tk.Label(self.window, text="Update Chapter Number:").grid(row=1, column=0,sticky="nsew")
        tk.Button(self.window, text="Select", borderwidth=1, relief="solid", command=lambda: self.update_cap_status()).grid(row=1, column=1,sticky="nsew")

        for i in range(2):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)
        self.window.attributes("-topmost", True)


    def update_new(self):

        for i in self.window.winfo_children():
            i.destroy()

        self.window.title()
        self.window.geometry("400x250+600+600")


        input_send_info_method = tk.StringVar()

        tk.Label(self.window, text="Use Standart method or Advanced? S/A").grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(self.window, text="S", command=lambda: (tk.Button.grid_forget, input_send_info_method.set("S"))).grid(row=1, column=0, sticky="nsew")
        tk.Button(self.window, text="A", command=lambda: (self.window.destroy(), input_send_info_method.set("A"))).grid(row=1, column=1, sticky="nsew")

        for i in range(2):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(0, weight=1)
        self.window.attributes("-topmost", True)

    def update_cap_status(self):

        self.window.destroy()