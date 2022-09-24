import time
from pygame import mixer
from mutagen.mp3 import MP3


mixer.init()
f = MP3('e:/VSC/Voice_Asistent_Pro/files/cache/main.mp3')
f = f.info.length
mixer.music.load("e:/VSC/Voice_Asistent_Pro/files/cache/main.mp3")
mixer.music.play()
time.sleep(f)