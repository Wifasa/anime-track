from datetime import datetime
import os
import tkinter as tk
from control import Control
from models.json_controls import Json_controls

current_Date = datetime.now()

pereza = ['One Punch Man',
'Jujutsu Kaisen',
'Sword Art Online',
'Sword Art Online II',
'Sword Art Online Movie: Ordinal Scale',
'Sword Art Online: Alicization',
'Sword Art Online: Alicization - War of Underworld',
'Boku no Hero Academia',
'Boku no Hero Academia 2nd Season',
'Boku no Hero Academia 3nd Season',
'Darling in the FranXX',
'Tate no Yuusha no Nariagari',
'Tensei shitara Slime Datta Ken',
'Plunderer',
'Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e Kayou',
'Maoujou de Oyasumi',
'Ore ga Ojousama Gakkou ni \"Shomin Sample\" Toshite Gets ❤ Sareta Ken',
'Kimetsu no Yaiba',
'Kimetsu no Yaiba Movie: Mugen Ressha-hen',
'Isekai wa Smarphone to Tomo ni.',
'Death March Kara Hajimaru Isekai KyousouKyoku',
'Trinity Seven',
'Trinity Seven Movie: Eternity Library to Alchemic Girl',
'Trinity Seven Movie 2: Tenkuu Toshokan to Shinku no Maou',
'Sentouin, Hakenshimasu!',
'Kenja no Mago',
'Assassins Pride',
'Zero no Tsukaima',
'Zero no Tsukaima: Futatsuki no Kishi',
'Zero no Tsukaima: Princess no Rondo',
'Zero no Tsukaima: Final',
'Kyokou Suiri',
'Kanojo, Okarishimasu',
'Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku you desu!',
'Kono Subarashii Sekai ni Shukufuku wo!',
'Kono Subarashii Sekai ni Shukufuku wo! 2',
'Date A Live',
'Date a Live II',
'Kono Subarashii Sekai ni Shukufuku wo!: Kurenai Densetsu',
'Date A Live Movie: Mayuri Judgment',
'Date A Live Ⅲ',
'Arifureta Shokugyou de Sekai Saikyou',
'Arifureta Shokugyou de Sekai Saikyou Specials',
'Murenase! Seton Gakuen',
'Akame ga Kill!',
'Kumo Desu ga, Nani ka?',
'Mushoku Tensei: Isekai Ittara Honki Dasu',
'Isekai Maou to Shoukan Shoujo no Dorei Majutsu',
'Isekai Maou to Shoukan Shoujo no Dorei Majutsu Ω',
'Hige wo Soru. Soshite Joshikousei wo Hirou',
'Tsugumomo',
'Tsugu Tsugumomo',
'Seiken Tsukai no World Break',
'Madan no Ou to Vanadis',
'No Game No Life: Zero',
'No Game No Life',
'Madan no Ou to Vanadis: Tigre-kun to Vanadi-chu',
'Kami-tachi ni Hirowareta Otoko',
'Rewrite',
'No Game No Life Specials',
'Rokudenashi Majutsu Koushi to Akashic Records',
'Kiseijuu: Sei no Kakuritsu',
'Tensei shitara Slime Datta Ken 2nd Season Part 2',
'Rewrite: Moon and Terra',
'Seirei Gensouki',
'Tsuki ga Michibiku Isekai Douchuu',
'Mairimashita! Iruma-kun',
'Mairimashita! Iruma-kun 2nd Season',
'Ore dake Haireru Kakushi Dungeon',
'Re:Zero kara Hajimeru Isekai Seikatsu',
'Re:Zero kara Hajimeru Isekai Seikatsu - Memory Snow',
'Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season',
'Edens Zero',
'Megami-ryou no Ryoubo-kun.',
'Overlord',
'Overlord II',
'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka',
'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka OVA',
'Overlord III',
'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka II',
'Isekai Cheat Magician',
'Maou-sama, Retry!',
'Meikyuu Black Company',
'Ichiban Ushiro no Daimaou',
'Ichiban Ushiro no Daimaou Specials',
'Shinmai Maou no Testament',
'Shinmai Maou no Keiyakusha Special',
'Shinmai Maou no Testament OVA',
'Shinmai Maou no Testament Burst',
'Maoyu Mao Yuusha',
'Seirei Tsukai no Blade Dance',
'Kaifuku Jutsushi no Yarinaoshi',
'Shinmai Maou no Testament Departures',
'Ao no Exorcist',
'Ange Vierge',
'High School DxD',
'High School DxD OVA',
'High School DxD New',
'High School DxD BorN',
'High School DxD BorN: Yomigaerarenai Pheonix',
'High School DxD Hero',
'Ao no Exorcist (Movie)',
'High School DxD BorN Specials',
'Gotoubun no Hanayome',
'Gotoubun no Hanayome 2nd Season',
'Gate: Jieitai Kanochi nite, Kaku Tatakaeri',
'Gate: Jieitai Kanochi nite, Kaku Tatakaeri - Enryuu-hen',
'Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru',
'Genjitsu Shugi Yuusha no Oukoku Saikenki',
'Musaigen no Phantom World',
'Absolute Duo',
'One Punch Man Specials',
'One Punch Man: Road to Hero',
'Fate/Grand Order: Zettai Majuu Sensen Babylonia - Initium Iter',
'Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen',
'Kimetsu no Yaiba: Mugen Ressha-hen Arc TV',
'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e (TV)',
'Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita',
'Mushoku Tensei: Isekai Ittara Honki Dasu Part 2',
'Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei',
'Takt Op. Destiny',
'Tensura Nikki: Tensei shitara Slime Datta Ken',
'Tsuki to Laika to Nosferatu',
'Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru',
'Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen',
'Netoge no Yome wa Onnanoko ja Nai to Omotta?',
'Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen 2nd Season',
'Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shima',
'Ore wo Suki nano wa Omae dake ka yo',
'Ore wo Suki nano wa Omae dake ka yo: Oretachi no Game Set',
'Kobayashi-san Chi no Maid Dragon',
'Kobayashi-san Chi no Maid Dragon S',
'Kobayashi-san Chi no Maid Dragon S Mini Dragon',
'Saihate no Paladin',
'Nanatsu no Taizai',
'Nanatsu no Taizai: Seisen no Shirushi',
'Nanatsu no Taizai: Imashime no Fukkatsu',
'Nanatsu no Taizai Movie: Tenkuu no Torawarebito',
'Nanatsu no Taizai: Kamigami no Gekirin',
'Nanatsu no Taizai: Fundo no Shinpan',
'Jitsu wa Watashi wa',
'Conception',
'Nanatsu no Taizai Movie 2: Hikari ni Norowareshi Mono-tachi',
'Sword Art Online: Extra Edition',
'Tensei shitara Slime Datta Ken OVA',
'100-man no Inochi no Ue ni Ore wa Tatteiru',
'100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season',
'Princess Connect! Re:Dive',
'Shironeko Project: Zero Chronicle',
'Masamune-kun no Revenge',
'Knight\'s & Magic',
'Ore no Kanojo to Osananajimi ga Shuraba Sugiru',
'Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore',
'Monster Musume no Oishasan',
'THE DAILY LIFE OF THE IMMORTAL KING',
'The Daily Life of the Immortal King 2nd Season',
'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka Gaiden: Sword Oratoria',
'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III',
'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka Movie: Orion no Ya',
'Kimetsu no Yaiba: Yuukaku-hen',
'Sousei no Onmyouji',
'Horimiya',
'Hori-san to Miyamura-kun',
'Dr. Stone',
'Dr. Stone: Stone Wars',
'Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu.',
'Kawaikereba Hentai demo Suki ni Natte Kuremasu ka?',
'Saijaku Muhai no Bahamut',
'Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai',
'Leadale no Daichi nite',
'Orient',
'Shikkakumon no Saikyou Kenja',
'Sono Bisque Doll wa Koi wo Suru',
'Seishun Buta Yarou wa Yumemiru Shoujo no Yume wo Minai',
'Tensai Ouji no Akaji Kokka Saisei Jutsu',
'Princess Connect! Re:Dive Season 2',
'Kenja no Deshi wo Nanoru Kenja',
'Fantasy Bishoujo Juniku Ojisan to',
'Koroshi Ai',
'Shuumatsu no Harem',
'Arifureta Shokugyou de Sekai Saikyou 2nd Season',
'Genjitsu Shugi Yuusha no Oukoku Saikenki',
'Dolls\' Frontline',
'Build Divide: Code Black',
'Net-juu no Susume',
'Otome Game Sekai wa Mob ni Kibishii Sekai desu',
'Yuusha, Yamemasu',
'Shijou Saikyou no Daimaou, Murabito A ni Tensei suru',
'Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu',
'Kaguya-sama wa Kokurasetai: Ultra Romantic',
'Spy x Family',
'Tate no Yuusha no Nariagari Season 2',
'RPG Fudousan',
'Dr. Stone: Ryuusui',
'Tensei Kenja no Isekai Life: Dai-2 no Shokugyou wo Ete, Sekai Saikyou ni Narimashita',
'Kinsou no Vermeil',
'Isekai Meikyuu de Harem wo',
'Kuro no Shoukanshi',
'Overlord IV',
'Yofukashi no Uta',
'Kanojo, Okarishimasu 2nd Season',
'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e (TV) 2nd Season',
'Isekai Yakkyoku',
'Jujutsu Kaisen 0 Movie',
'Tensei shitara Ken Deshita',
'Noumin Kanren no Skill bakka Agetetara Nazeka Tsuyoku Natta.',
'THE DAILY LIFE OF THE IMMORTAL KING 3',
'Yuusha Party wo Tsuihou sareta Beast Tamer, Saikyoushu no Nekomimi Shoujo to Deau',
'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka IV: Shin Shou - Meikyuu-hen',
'Mahoutsukai Reimeiki',
'Chainsaw Man',
'Hataraku Maou-sama!!',
'Busou Shoujo Machiavellianism',
'Mamahaha no Tsurego ga Motokano datta',
'Akuyaku Reijou nanode Last Boss wo Kattemimashita',
'Kage no Jitsuryokusha ni Naritakute!',
'Orient 2ª temp (cap 24)',
'Mairimashita! Iruma-kun 3rd Season',
'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka IV',
'Tensei Oujo to Tensai Reijou no Mahou Kakumei',
'Hyouken no Majutsushi ga Sekai wo Suberu',
'Kami-tachi ni Hirowareta Otoko 2nd Season',
'Isekai Nonbiri Nouka',
'Tondemo Skill de Isekai Hourou Meshi',
'Shin Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei',
'Kaiko sareta Ankoku Heishi (30-dai) no Slow na Second Life',
'Saikyou Onmyouji no Isekai Tenseiki',
'Ningen Fushin no Boukensha-tachi ga Sekai wo Sukuu you desu',
'Goblin Slayer',
'Tensei shitara Slime Datta Ken Movie: Guren no Kizuna-hen',
'Spy Kyoushitsu',
'Isekai Ojisan',
'Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2',
'Kyokou Suiri Season 2',
'Black Clover: Mahou Tei no Ken',
'Tensei Kizoku no Isekai Boukenroku: Jichou wo Shiranai Kamigami no Shito',
'Kimetsu no Yaiba: Katanakaji no Sato-hen',
'Isekai wa Smartphone to Tomo ni. 2',
'Dr. Stone: New World',
'Isekai One Turn Kill Neesan: Ane Douhan no Isekai Seikatsu Hajimemashita',
'Isekai Shoukan wa Nidome desu',
'Dead Mount Death Play',
'Iseleve',
'Mashle',
'Jigokuraku',
'Kaminaki Sekai no Kamisama Katsudou',
'Kono Subarashii Sekai ni Bakuen wo!',
'Ryza no Atelier: Tokoyami no Joou to Himitsu no Kakurega',
'Okashi na Tensei',
'Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou',
'Seija Musou: Salaryman, Isekai de Ikinokoru Tame ni Ayumu Michi',
'Mushoku Tensei II: Isekai Ittara Honki Dasu',
'Level 1 dakedo Unique Skill de Saikyou desu',
'Maou Gakuin no Futekigousha II',
'Jitsu wa Ore, Saikyou deshita?',
'Eiyuu Kyoushitsu',
'Tensei shitara Slime Datta Ken: Coleus no Yume',
'Nanatsu no Maken ga Shihai suru',
'Kage no Jitsuryokusha ni Naritakute! 2nd Season',
'Dr. Stone: New World',
'Tate no Yuusha no Nariagari Season 3',
'Saihate no Paladin: Tetsusabi no Yama no Ou',
'Jujutsu Kaisen 2nd Season',
'Zom 100: Zombie ni Naru made ni Shitai 100 no Koto',
'Seiken Gakuin no Makentsukai',
'Kikansha no Mahou wa Tokubetsu desu',
'Hametsu no Oukoku',
'Nozomanu Fushi no Boukensha',
'Saikyou Tank no Meikyuu Kouryaku',
'Sasaki to Pii-chan',
'Sokushi Cheat ga Saikyou sugite, Isekai no Yatsura ga Marude Aite ni Naranai n desu ga.',
'Mato Seihei no Slave',
'Isekai de Mofumofu Nadenade suru Tame ni Ganbattemasu.',
'Kekkon Yubiwa Monogatari',
'Ishura',
'Himesama \"Goumon\" no Jikan desu',
'Akuyaku Reijou Level 99: Watashi wa Ura-Boss desu ga Maou dewa Arimasen',
'Gekai Elise',
'Shin no Nakama S2',
'Chiyu Mahou no Machigatta Tsukaikata',
'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 3rd Season',
'Mashle temp2 (24 caps) ',
'Saijaku Tamer wa Gomi Hiroi no Tabi wo Hajimemashita.',
'Loop 7-kaime no Akuyaku Reijou wa',
'Shangri-La Frontier: Kusoge Hunter, Kamige ni Idoman to su',
'Ore dake Level Up na Ken',
'Maou no Ore ga Dorei Elf wo Yome ni Shitanda ga, Dou Medereba Ii?',
'Re:Monster',
'Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu',
'Dekisokonai to Yobareta Motoeiyuu wa Jikka kara Tsuihou sareta node Sukikatte ni Ikiru Koto ni Shita',
'Dungeon Meshi',
'Tensei Kizoku, Kantei Skill de Nariagaru',
'Tsuki ga Michibiku Isekai Douchuu 2nd Season',
'Lv2 kara Cheat datta Motoyuusha Kouho no Mattari Isekai Life**',
'The New Gate',
'Kaijuu 8-gou',
'Mushoku Tensei II: Isekai Ittara Honki Dasu',
'Kimetsu no Yaiba: Hashira Geiko-hen',
'Kami no Tō',
'Ragna Crimson',
'Ore wa Subete wo \"Parry\" suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai',
'Isekai Yururi Kikou: Kosodateshinagara Boukensha Shimasu',
'Mob kara Hajimaru Tansaku Eiyuutan',
'Maougun Saikyou no Majutsushi wa Ningen datta',
'Shinmai Ossan Boukensha, Saikyou Party ni Shinu hodo Kitaerarete Muteki ni Naru.',
'Sousou no Frieren',
'Hazurewaku no \"Joutai Ijou Skill\" de Saikyou ni Natta Ore ga Subete wo Juurin suru made',
'Isekai Shikkaku',
'Tensei shitara Slime Datta Ken 3rd Season',
'Maou Gakuin no Futekigousha II',
'Tsue to Tsurugi no Wistoria',
'Naze Boku no Sekai wo Daremo Oboeteinai no ka?',
'Ao no Exorcist: Kyoto Fujouou-hen',
'Ao no Exorcist: Kyoto Fujouou-hen OVA',
'Ao no Exorcist: Shimane Illuminati-hen',
'Hitoribocchi no Isekai Kouryaku',
'Maou-sama, Retry! R',
'Saikyou no Shienshoku \"Wajutsushi\" de Aru Ore wa Sekai Saikyou Clan wo Shitagaeru',
'Dandadan',
'Sayounara Ryuusei, Konnichiwa Jinsei',
'Party kara Tsuihou sareta Sono Chiyushi, Jitsu wa Saikyou ni Tsuki',
'Kimi wa Meido-sama.',
'Nageki no Bourei wa Intai shitai',
'Tensei Kizoku, Kantei Skill de Nariagaru',
'Seirei Gensouki 2',
'Rekishi ni Nokoru Akujo ni Naru zo',
'Mecha-ude (TV)',
'Kami wa Game ni Ueteiru.',
'Kami no Tou: Ouji no Kikan',
'Ao no Exorcist: Yuki no Hate-hen',
'Benriya Saitou-san, Isekai ni Iku',
'Youjo Senki',
'Youjo Senki Movie',
'Isekai Quartet',
'Isekai Quartet 2nd Season',
'Isekai Quartet Movie: Another World',
'Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi♀']

# print(datetime.now().isoformat())

def clear_window():
    os.system('cls' if os.name == "nt" else "clear")

# def window_update_new_close(input_name,input_Current_Cap,dic_emi,window):
#     name = input_name.get()
#     Current_Cap = input_Current_Cap.get()

#     dic_temp={
#         "Id": ((dic_emi[-1][next(iter(dic_emi[-1]))])) + 1,
#         "Values":{
#             "Name": name,
#             "Day": current_Date.strftime("%A"),
#             "Current_Cap": Current_Cap,
#             "Status": "emission",
#             "Date&Time": datetime.now().isoformat()
#         }
#     }
#     dic_emi.append(dic_temp)
#     window.destroy() 
    
#     return dic_emi

# def update_new():

#     window_menu.destroy()

#     input_send_info_method = window_tk.update_new()
#     dic_emi=Json_controls.get_anime_emi_data()

#     window_send_info_method = tk.Tk()
#     window_send_info_method.title()
#     window_send_info_method.geometry("400x250+600+600")


#     input_send_info_method = tk.StringVar()

#     tk.Label(window_send_info_method, text="Use Standart method or Advanced? S/A").grid(row=0, column=0, columnspan=2, sticky="nsew")
#     tk.Button(window_send_info_method, text="S", command=lambda: (tk.Button.grid_forget, input_send_info_method.set("S"))).grid(row=1, column=0, sticky="nsew")
#     tk.Button(window_send_info_method, text="A", command=lambda: (window_send_info_method.destroy(), input_send_info_method.set("A"))).grid(row=1, column=1, sticky="nsew")

#     for i in range(2):
#         window_send_info_method.grid_rowconfigure(i, weight=1)
#         window_send_info_method.grid_columnconfigure(0, weight=1)
#     window_send_info_method.attributes("-topmost", True)

#     window_send_info_method.mainloop()

#     send_info_method = input_send_info_method.get()

#     if send_info_method.upper() == "A":

#         names = []
#         day = ''
#         Current_Cap = []
#         status = "emission"
#         Date_Time = None #datetime.now().isoformat()
#         counter_Id = dic_emi[-1][next(iter(dic_emi[-1]))]

#         for i in range(len(names)):
#             counter_Id += 1

#             dic_temp={
#                 "Id": counter_Id,
#                 "Values":{
#                     "Name": names[i],
#                     "Day": day,
#                     "Current_Cap": Current_Cap[i],
#                     "Status": status,
#                     "Date&Time": None
#                 }
#             }

#             dic_emi.append(dic_temp)

#     else:
#         window = tk.Tk()
#         window.title("New Anime Add")

#         window.geometry("400x250+600+600")

#         tk.Label(window, text="Name:").grid(row=0, column=0,sticky="nsew")
#         input_name = tk.Entry(window)
#         input_name.grid(row=1, column=0,sticky="nsew")

#         tk.Label(window, text="Cap:").grid(row=2, column=0,sticky="nsew")
#         input_Current_Cap = tk.Entry(window)
#         input_Current_Cap.grid(row=3, column=0,sticky="nsew")

#         tk.Button(window, text="Send", command=lambda: window_update_new_close(input_name,input_Current_Cap,dic_emi,window)).grid(row=4, column=0,sticky="nsew")

#         for i in range(5):
#             window.grid_rowconfigure(i, weight=1)
#         window.grid_columnconfigure(0, weight=1)
#         window.attributes("-topmost", True)

#         window.mainloop()

#     Json_controls.save_anime_emi_data(dic_emi)

#     clear_window()

def update_cap_status(window_menu):

    window_menu.destroy()
    dic_emi_day = []

    dic_emi = Json_controls.get_anime_emi_data()

    print('Update current day chapter? y/n')
    choice = (input(''))

    if choice.lower() == 'y':
        day_name = current_Date.strftime("%A")
    else:
        day_options = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
        print('Choice day')
        for i in day_options:
            print(f'Nº: {i}\t{day_options[i]}')
        try:
            day_name = day_options[int(input(''))]
        except:
            print('Error value')
    
    for i in dic_emi:
        if i["Values"]["Day"] == day_name: # type: ignore
            dic_emi_day.append(i)

    for i in dic_emi_day:
        print(f'Id: {i["Id"]} - Name: {i["Values"]["Name"]}')

    print("Selec anime with id to update chapter number")

    try:
        chapter_update = int(input(""))
    except:
        print('Incorrect value, try again')
        chapter_update = int(input(""))

    print('Did you wan\'t to update more than one chapter? y/n defaul: N')
    chapter_update_number_multiple_value = input('')

    if chapter_update_number_multiple_value.lower() == 'y':
        print('Introduce how many chapters you wan\'t to add.')
        chapter_update_number = input('')
    else:
        chapter_update_number = 1
    
    for i in dic_emi:
        if i["Id"] == chapter_update:
            i["Values"]["Current_Cap"] = ((i["Values"]["Current_Cap"])+chapter_update_number)
            i["Values"]["Date&Time"] = datetime.now().isoformat()
    
    Json_controls.save_anime_emi_data(dic_emi)

    clear_window()

if __name__ == "__main__":
    
    control = Control()

    control.control_window_main_menu()