from pygame.mixer import music
from .dbJson import readjson
from .Duration import duration
from datetime import datetime


class play():
    def __init__(self):
        music.play()
        data = datetime.now()
        readjson.SetStartTime(readjson,f"{data.hour}:{data.minute}:{data.second}")
        duration()