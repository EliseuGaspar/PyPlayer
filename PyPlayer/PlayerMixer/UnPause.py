import pygame
from pygame.mixer import music


class unpause():
    # ...
    # ...
    def __init__(self):
        try:
            music.unpause()
        except pygame.error:
            print(
                "PyPayer.Error: Não é possível dar o unpause porque não houve um play()"
            )