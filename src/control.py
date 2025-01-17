from view.windows_tk import Windows_tk
from models.main_functions import Main_functions

class Control:
    def __init__(self) -> None:
        self.window_tk = Windows_tk()
        self.main_funtions = Main_functions()

    def control_window_main_menu(self):
        input_send_info_method = self.window_tk.window_main_menu()

    def control_update_new_anime_seeing(self):
