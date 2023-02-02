import pygame
from pygame.mixer import music
from .dbJson import readjson

class unpause():
    def __init__(self):
        try:
            music.unpause()
            readjson.SetStatusTime(
                readjson,
                True
            )
        except pygame.error:
            print(
                "PyPayer.Error: Não é possível dar o unpause porque não houve um play()"
            )