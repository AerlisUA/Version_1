import time; import os; os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from mutagen.mp3 import MP3
mixer.init()
def soundplay(file):
    try:
        f = MP3(file)
        f = f.info.length
        mixer.music.load(file)
        mixer.music.play()
        time.sleep(f)
        mixer.quit()
    except:
        mixer.init();soundplay(file)