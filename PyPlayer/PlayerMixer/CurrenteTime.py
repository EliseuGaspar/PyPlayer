from mutagen.mp3 import MP3
from datetime import datetime
from .dbJson import readjson
from .Duration import duration
from pygame.mixer import music
from time import sleep

def current_time(type_ : str = 'time', controler : bool = False, repeat : bool = False):
    readjson_ = readjson()
    time_current_file = int(readjson_.GetCurrentTime())
    full_time = int(readjson_.GetFileTime())
    if type_ == 'time':
        if not controler:
            sleep(0.8)
        if music.get_busy():
            if not repeat:
                if full_time != time_current_file:
                    readjson_.SetCurrentTime(str(time_current_file+1))
            minute = int(time_current_file/60)
            seconds = int(time_current_file%60)

            if minute < 10: minute = f"0{minute}"
            if seconds < 10: seconds = f"0{seconds}"

            return f"{minute}:{seconds}"
        else:
            if readjson.GetStatusTime(readjson):
                return True
            minute = int(time_current_file/60)
            seconds = int(time_current_file%60)

            if minute < 10: minute = f"0{minute}"
            if seconds < 10: seconds = f"0{seconds}"

            return f"{minute}:{seconds}"
    elif type_ == 'size':
        if not controler:
            sleep(0.8)
        if music.get_busy():
            if not repeat:
                if full_time != time_current_file:
                    readjson_.SetCurrentTime(str(time_current_file+1))
        else:
            if readjson.GetStatusTime(readjson):
                return True
        return time_current_file
    else:
        return 0

        

