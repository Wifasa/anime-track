from datetime import datetime
import os
from .json_controls import Json_controls


class Main_functions:
    def update_new_anime_seeing(self, input_send_info_method):

        dic_emi=Json_controls.get_anime_emi_data()

        send_info_method = input_send_info_method.get()

        if send_info_method.upper() == "A":

            names = []
            day = ''
            Current_Cap = []
            status = "emission"
            Date_Time = None #datetime.now().isoformat()
            counter_Id = dic_emi[-1][next(iter(dic_emi[-1]))]

            for i in range(len(names)):
                counter_Id += 1

                dic_temp={
                    "Id": counter_Id,
                    "Values":{
                        "Name": names[i],
                        "Day": day,
                        "Current_Cap": Current_Cap[i],
                        "Status": status,
                        "Date&Time": None
                    }
                }

                dic_emi.append(dic_temp)

        # else:
        #     window = tk.Tk()
        #     window.title("New Anime Add")

        #     window.geometry("400x250+600+600")

        #     tk.Label(window, text="Name:").grid(row=0, column=0,sticky="nsew")
        #     input_name = tk.Entry(window)
        #     input_name.grid(row=1, column=0,sticky="nsew")

        #     tk.Label(window, text="Cap:").grid(row=2, column=0,sticky="nsew")
        #     input_Current_Cap = tk.Entry(window)
        #     input_Current_Cap.grid(row=3, column=0,sticky="nsew")

        #     tk.Button(window, text="Send", command=lambda: window_update_new_close(input_name,input_Current_Cap,dic_emi,window)).grid(row=4, column=0,sticky="nsew")

        #     for i in range(5):
        #         window.grid_rowconfigure(i, weight=1)
        #     window.grid_columnconfigure(0, weight=1)
        #     window.attributes("-topmost", True)

        #     window.mainloop()

        Json_controls.save_anime_emi_data(dic_emi)
