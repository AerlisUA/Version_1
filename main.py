import os
from functions import Aeris
from sys import exit as end


Aeris().check_modules()
Aeris().check_region()

while 1:
    try:
        command = Aeris().record()
        print(command)
    except:
        if not os.path.exists("files/cache"):
            os.makedirs("files/cache")
            continue
        end(1)
    commands = {"відкрий браузер": Aeris().open_browser,
    "відкрити браузер": Aeris().open_browser,
    "відкрвай браузер": Aeris().open_browser,
    "відкрий браузер": Aeris().open_browser,
    "інформація про ip": Aeris().ip_info,
    "вихід": Aeris().off,
    "пошук youtube": Aeris().search_youtube,
    "скільки часу": Aeris().check_time,
    "скільки зараз часу": Aeris().check_time,
    "скіки часу": Aeris().check_time,
    "завантажити відео youtube": Aeris().download_youtube_mp4,
    'створити проект в google colab': Aeris().create_googleColab,
    'запустити командну строку': Aeris().start_Aerlis_console,
    "": Aeris().null
    } 
    commands.get(command, Aeris().check__a_question)()