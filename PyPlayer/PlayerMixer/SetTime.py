from pygame.mixer import music
from .dbJson import readjson


class settime():
    def __init__(self,pos : float = None):
        if pos != None:
            music.set_pos(pos)
            readjson.SetCurrentTime(readjson,str(int(pos)))
