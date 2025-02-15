import json
import os


class Json_controls:
    
    @staticmethod
    def get_anime_emi_data():

        try:
            with open('\\\\Casa-JJ\\Estudios\\PROYECTOS\\anime-track\\src\\data\\anime-emission.json', 'r') as emission:
                dic_emi = json.load(emission)
        except:
            with open('src\\data\\anime-emission.json', 'r') as emission:
                dic_emi = json.load(emission)
        return dic_emi

    @staticmethod
    def save_anime_emi_data(dic_emi):

        try:
            with open('\\\\Casa-JJ\\Estudios\\PROYECTOS\\anime-track\\src\\data\\anime-emission.json', 'w') as emission:
                json.dump(dic_emi,emission, indent=4)
        except:
            with open('src\\data\\anime-emission.json', 'w') as emission:
                json.dump(dic_emi,emission, indent=4)

    @staticmethod
    def local_save():

        try:
            with open('\\\\Casa-JJ\\Estudios\\PROYECTOS\\anime-track\\src\\data\\config.json', 'r') as config_config:
                config = json.load(config_config)
        except:
            with open('src\\data\\config.json', 'w') as config_config:
                config = json.load(config_config)


class Misc:

    @staticmethod
    def clear_window():

        os.system('cls' if os.name == "nt" else "clear")