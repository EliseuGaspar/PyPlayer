from pygame.mixer import music

def setvolume(volume:float): music.set_volume(volume)

def getvolume(): return music.get_volume()