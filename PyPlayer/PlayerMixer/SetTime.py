from pygame.mixer import music


class settime():
    def __init__(self,pos : float = None):
        if pos != None:
            music.set_pos(pos)
