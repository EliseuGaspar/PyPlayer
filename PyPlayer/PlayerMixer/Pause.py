import pygame
from pygame.mixer import music
from .dbJson import readjson


class pause():
    def __init__(self , *args):
        music.pause()
        readjson.SetStatusTime(
            readjson,
            False
        )