import pygame
from pygame.mixer import music
from .dbJson import readjson
from .Duration import duration
from datetime import datetime


class play():
    # ...
    # ...
    def __init__(self):
        self.readjson = readjson()
        try:
            music.play()
            data = datetime.now()
            self.readjson.SetStartTime(f"{data.hour}:{data.minute}:{data.second}")
            self.readjson.SetCurrentTime(new_time='0')
            duration()
        except pygame.error:
            print(
                "PyPayer.Error: Não é possível dar o play porque não foi feito nenhum load()"
            )