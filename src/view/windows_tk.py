import tkinter as tk
from models.main_functions import Main_functions
class Windows_tk:

    def __init__(self):
        self.window = tk.Tk()
        self.main_functions = Main_functions()

    def window_main_menu(self):
        
        
        self.window.title("Main menu")

        self.window.geometry("400x250+600+600")

        tk.Label(self.window, text="Add New Amime:").grid(row=0, column=0,sticky="nsew")
        tk.Button(self.window, text="Select", borderwidth=1, relief="solid", command=lambda: self.update_new_anime_seeing()).grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        tk.Label(self.window, text="Update Chapter Number:").grid(row=1, column=0,sticky="nsew")
        tk.Button(self.window, text="Select", borderwidth=1, relief="solid", command=lambda: self.update_anime_cap_status()).grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        for i in range(2):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)
        self.window.attributes("-topmost", True)

        self.window.mainloop()

    def clear_grid(self):
        for i in self.window.winfo_children():
            i.destroy()


    def update_new_anime_seeing(self):

        self.clear_grid()

        self.window.title()

        tk.Label(self.window, text="Use Standart method or Advanced? S/A").grid(row=0, column=0, columnspan=2)
        tk.Button(self.window, text="S", borderwidth=1, relief="solid", command=lambda: (self.standart_add_anime())).grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        tk.Button(self.window, text="A", borderwidth=1, relief="solid", command=lambda: (self.main_functions.update_new_anime_seeing())).grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        for i in range(2):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(0, weight=1)
        self.window.attributes("-topmost", True)

    def standart_add_anime(self):
        
        self.clear_grid()
        self.window.title("New Anime Add")
        self.window.geometry("400x250+600+600")

        tk.Label(self.window, text="Name:").grid(row=0, column=0,columnspan=2)
        input_name = tk.Entry(self.window, borderwidth=1, relief="solid", justify="center")
        input_name.grid(row=1, column=0, columnspan=2, padx=10, pady=5,sticky="nsew")

        tk.Label(self.window, text="Cap:").grid(row=2, column=0,sticky="nsew")
        input_Current_Cap = tk.Entry(self.window, borderwidth=1, relief="solid", justify="center")
        input_Current_Cap.grid(row=2, column=1, padx=10, pady=5,sticky="nsew")

        tk.Button(self.window, text="Send", borderwidth=1, relief="solid", command=lambda: self.main_functions.window_update_new_standart(input_name,input_Current_Cap)).grid(row=4, column=0, columnspan=2)

        for i in range(5):
            self.window.grid_rowconfigure(i, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        
        self.window.attributes("-topmost", True)

    def update_anime_cap_status(self):

        self.clear_grid()

        self.window.title()
        input_send_info_method = tk.StringVar()

        tk.Label(self.window, text="Update current day chapter? y/n").grid(column=0, row=0, columnspan=2)
        tk.Button(self.window, text="Y", borderwidth=1, relief="solid", command=lambda: input_send_info_method.set("Y")).grid(column=0, row=1, sticky="nsew")
        tk.Button(self.window, text="N", borderwidth=1, relief="solid", command=lambda: self.update_anime_cap_status_day_select()).grid(column=1, row=1, sticky="nsew")

        for i in range(2):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)
        self.window.attributes("-topmost", True)

    def update_anime_cap_status_day_select(self):

        self.clear_grid()

        self.window.title("Day select")
        input_day_choice = tk.StringVar(value="")

        tk.Label(self.window, text="Select day.", ).grid(column=0, row=0, sticky="nsew")
        tk.Checkbutton(self.window, text="1.- Monday", variable=input_day_choice, onvalue="Monday", offvalue="").grid(column=0, row=1, sticky="nsew")
        tk.Checkbutton(self.window, text="2.- Tuesday", variable=input_day_choice, onvalue="Tuesday", offvalue="").grid(column=0, row=2, sticky="nsew")
        tk.Checkbutton(self.window, text="3.- Wednesday", variable=input_day_choice, onvalue="Wednesday", offvalue="").grid(column=0, row=3, sticky="nsew")
        tk.Checkbutton(self.window, text="4.- Thursday", variable=input_day_choice, onvalue="Thursday", offvalue="").grid(column=0, row=4, sticky="nsew")
        tk.Checkbutton(self.window, text="5.- Friday", variable=input_day_choice, onvalue="Friday", offvalue="").grid(column=0, row=5, sticky="nsew")
        tk.Checkbutton(self.window, text="6.- Saturday", variable=input_day_choice, onvalue="Saturday", offvalue="").grid(column=0, row=6, sticky="nsew")
        tk.Checkbutton(self.window, text="7.- Sunday", variable=input_day_choice, onvalue="Sunday", offvalue="").grid(column=0, row=7, sticky="nsew")
        tk.Button(self.window, text="Select", borderwidth=1, relief="solid", command=lambda: self.clear_grid).grid(column=0, row=8, sticky="nsew")

        for i in range(8):
            self.window.grid_rowconfigure(i, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.attributes("-topmost", True)