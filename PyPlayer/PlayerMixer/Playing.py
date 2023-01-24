from pygame.mixer import music

def playing():
    if music.get_busy():
        return True
    else:
        return False
