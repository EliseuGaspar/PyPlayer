import pygame
from pygame.mixer import music


class pause():
    def __init__(self , *args):
        if args:
            print(
                "PyPlayer.Error: pause() não recebe nenhum valor"
            )
        else:
            music.pause()