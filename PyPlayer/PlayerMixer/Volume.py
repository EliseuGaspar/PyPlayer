import pygame
from pygame.mixer import music


def setvolume(volume:float):
    if type(volume) is float:
        music.set_volume(volume)
    else:
        print(
            "PyPlayer.Error: O metódo set_volume só recebe valores do tipo float"
        )

def getvolume(): return music.get_volume()