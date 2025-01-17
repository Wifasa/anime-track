import tkinter as tk

class Windows_tk:

    def __init__(self):
        self.window = tk.Tk()

    def window_main_menu(self):
        
        
        self.window.title("Main menu")

        self.window.geometry("400x250+600+600")

        tk.Label(self.window, text="Add New Amime:").grid(row=0, column=0,sticky="nsew")
        tk.Button(self.window, text="Select", borderwidth=1, relief="solid", command=lambda: self.main_funtions.update_new_anime_seeing()).grid(row=0, column=1,sticky="nsew")

        tk.Label(self.window, text="Update Chapter Number:").grid(row=1, column=0,sticky="nsew")
        tk.Button(self.window, text="Select", borderwidth=1, relief="solid", command=lambda: self.update_cap_status()).grid(row=1, column=1,sticky="nsew")

        for i in range(2):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)
        self.window.attributes("-topmost", True)

        self.window.mainloop()

    def clear_grid(self):
        for i in self.window.winfo_children():
            i.destroy()


    def update_new(self):

        self.clear_grid()

        self.window.title()

        input_send_info_method = tk.StringVar()

        tk.Label(self.window, text="Use Standart method or Advanced? S/A").grid(row=0, column=0, columnspan=2)
        tk.Button(self.window, text="S", borderwidth=1, relief="solid", command=lambda: (input_send_info_method.set("S"))).grid(row=1, column=0, sticky="nsew")
        tk.Button(self.window, text="A", borderwidth=1, relief="solid", command=lambda: (input_send_info_method.set("A"))).grid(row=1, column=1, sticky="nsew")

        for i in range(2):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(0, weight=1)
        self.window.attributes("-topmost", True)

        return input_send_info_method

    def update_cap_status(self):

        self.clear_grid()

        self.window.title()
        input_send_info_method = tk.StringVar()

        tk.Label(self.window, text="Update current day chapter? y/n", ).grid(column=0, row=0, columnspan=2)
        tk.Button(self.window, text="Y", borderwidth=1, relief="solid", command=lambda: input_send_info_method.set("Y")).grid(column=0, row=1, sticky="nsew")
        tk.Button(self.window, text="N", borderwidth=1, relief="solid", command=lambda: input_send_info_method.set("N")).grid(column=1, row=1, sticky="nsew")

        for i in range(2):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)
        self.window.attributes("-topmost", True)

window_tk = Windows_tk()
window_tk.window_main_menu()