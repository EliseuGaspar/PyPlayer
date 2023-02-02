from pygame.mixer import music
from .dbJson import readjson

class stop():
    def __init__(self):
        music.stop()
        readjson.SetCurrentTime(
            readjson,
            "0"
        )
        readjson.SetStatusTime(
            readjson,
            False
        )