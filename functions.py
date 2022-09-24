import os, sys, time, pyautogui
import files.play_sound as play_sound
import speech_recognition
from gtts import gTTS
from files.download_video_youtube import downloadYouTube as d_y_t
from datetime import datetime



recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()
"""
Init speech_recognition
"""
class Aeris:
    def __init__(self):
        self.name = 'Aeris'
    
    def record(self):
        with microphone:
            recorded_data = ""
            recognizer.adjust_for_ambient_noise(microphone, duration=2)
            try:
                print("Program: Кажіть")
                audio = recognizer.listen(microphone, 5, 5)
                with open("files/cache/microphone-results.wav", "wb") as file:
                    file.write(audio.get_wav_data())
            except speech_recognition.WaitTimeoutError:
                return
            try:
                recorded_data = recognizer.recognize_google(audio, language="uk").lower()
            except speech_recognition.UnknownValueError:
                pass
            except speech_recognition.RequestError:
                print("Program: Увімкніть інтернет")
        os.remove("files/cache/microphone-results.wav")
        return recorded_data

    def check_region(self):
        os.system('python files/checking.py')
        
    def speak(self, massage_speak):
        tts = gTTS(text=massage_speak, lang='uk', slow = False)
        tts.save("files/cache/main.mp3")
        "Saving voice in mp3 file"
        time.sleep(1)
        play_sound.soundplay("files/cache/main.mp3")

    def start_Aerlis_console(self):
        if sys.platform == "linux" or sys.platform == "linux2":
            self.speak("Вибачте. але данна функція працює лише на виндовс")
        elif sys.platform == "win32":
            self.speak('Запуск Аю ком Андну строк У аєрл Іс')
            print('Запуск консоли')

    def open_site(self, site):
        if sys.platform == "linux" or sys.platform == "linux2":
            os.system(f'{site}')
        elif sys.platform == "win32":
            os.system(f'start explorer {site}')

    def open_browser(self):
        self.speak('відкриваю браузер')
        if sys.platform == "linux" or sys.platform == "linux2":
            os.system(f'"https://"')
        elif sys.platform == "win32":
            os.system('start explorer "https://"')

    def search_music(self):
        self.speak('Що будемо шукати')
        name = self.record()
        os.system(f'start explorer "https://google.com/search?q={name}+music"')

    def search_video(self):
        self.speak('Що будемо шукати')
        name = self.record()
        if sys.platform == "linux" or sys.platform == "linux2":
            os.system(f'"https://google.com/search?q={name}&sxsrf=ALiCzsZ4FqbeJLXhlYTWCnod8FE--R64_w:1661866438619&source=lnms&tbm=vid&sa=X&ved=2ahUKEwiyuPP11u75AhWNxosKHVliC1QQ_AUoAnoECAIQBA&cshid=1661866523975131&biw=1920&bih=961&dpr=1"')
        elif sys.platform == "win32":
            os.system(f'start explorer "https://google.com/search?q={name}&sxsrf=ALiCzsZ4FqbeJLXhlYTWCnod8FE--R64_w:1661866438619&source=lnms&tbm=vid&sa=X&ved=2ahUKEwiyuPP11u75AhWNxosKHVliC1QQ_AUoAnoECAIQBA&cshid=1661866523975131&biw=1920&bih=961&dpr=1"')
    
    def search_youtube(self):
        self.speak('Що будемо шукати')
        name = self.record()
        if sys.platform == "linux" or sys.platform == "linux2":
            os.system(f'"https://www.youtube.com/results?search_query={name}"')
        elif sys.platform == "win32":
            os.system(f'start explorer "https://www.youtube.com/results?search_query={name}"')

    def null(self):
        pass

    def error(self):
        self.speak('Вибачте, але я не розумію')

    def ip_info(self):
        os.system('start pythonw files/ip-info.py')

    def check_modules(self):
        os.system('python files/check_modules.py')

    def check_time(self):
        m = datetime.now()
        self.speak(f'Зараз {m.hour} {m.minute}')

    def check__a_question(self):
        self.error()

    def download_youtube_mp4(self):
        self.speak('уведІть посилання на відео')
        G = input('Посилання : ')
        self.speak('завант Ажую відео для вас, це може зайняти декілька хвилин')
        try:
            d_y_t(G, path='Downloads')
            self.speak('відео завантажено')
        except:
            self.speak('Сталася помилка. Посилання яке ви ввели не коректне')

    def download_youtube_mp3(self):
        self.speak('уведІть посилання на відео')
        G = input('Посилання : ')
        self.speak('завант Ажую аудіо для вас, це може зайняти декілька хвилин')
        try:
            d_y_t(G, path='Downloads', file_extension='mp3')
            self.speak('відео завантажено')
        except:
            self.speak('Сталася помилка. Посилання яке ви ввел И не кор Ектне')

    def create_googleColab(self):
        os.system('explorer "https://colab.research.google.com/#create=true"')

    def decstop_l(self):
        pyautogui.keyDown('win') 
        pyautogui.keyDown('ctrl')
        pyautogui.press('left') 
        pyautogui.keyUp('win')
        pyautogui.keyUp('ctrl')

    def decstop_r(self):
        pyautogui.keyDown('win') 
        pyautogui.keyDown('ctrl')
        pyautogui.press('right') 
        pyautogui.keyUp('win')
        pyautogui.keyUp('ctrl')

    def off(self):
        self.speak("Вимик Аюсь")
        try:
            os.remove("files/cache/main.mp3")
        except:
            pass
        sys.exit(1)