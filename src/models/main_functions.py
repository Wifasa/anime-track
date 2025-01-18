from datetime import datetime
import os
from .json_controls import Json_controls
from datetime import datetime


class Main_functions:
    def __init__(self) -> None:
        self.current_Date = datetime.now()
        self.dic_emi = Json_controls.get_anime_emi_data()

    def update_new_anime_seeing(self):

        names = []
        day = ''
        Current_Cap = []
        status = "emission"
        Date_Time = datetime.now().isoformat()
        counter_Id = self.dic_emi[-1][next(iter(self.dic_emi[-1]))]

        for i in range(len(names)):
            counter_Id += 1

            dic_temp={
                "Id": counter_Id,
                "Values":{
                    "Name": names[i],
                    "Day": day,
                    "Current_Cap": Current_Cap[i],
                    "Status": status,
                    "Date&Time": Date_Time
                }
            }

            self.dic_emi.append(dic_temp)

        Json_controls.save_anime_emi_data(self.dic_emi)

    def window_update_new_standart(self, input_name, input_Current_Cap):
        name = input_name.get()
        Current_Cap = input_Current_Cap.get()

        dic_temp={
            "Id": ((self.dic_emi[-1][next(iter(self.dic_emi[-1]))])) + 1,
            "Values":{
                "Name": name,
                "Day": self.current_Date.strftime("%A"),
                "Current_Cap": Current_Cap,
                "Status": "emission",
                "Date&Time": datetime.now().isoformat()
            }
        }
        self.dic_emi.append(dic_temp) 
        
        Json_controls.save_anime_emi_data(self.dic_emi)