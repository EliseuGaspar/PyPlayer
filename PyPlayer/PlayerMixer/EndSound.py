from pygame.mixer import music

def endsound(): 
    y = 2
    for x in range(0,y+1):
        y+=2
        return music.get_busy()