from mutagen.mp3 import MP3
from datetime import datetime
from .dbJson import readjson
from .Duration import duration
from pygame.mixer import music
from time import sleep

"""
def newtime(time1,time2):
    
    usertime = 100 - time1
    percentagem = (usertime*time2)/100

    return time2 - percentagem

def currenttime(endtime : int = 100):
    
    data = datetime.now()
    
    start_time = readjson.GetStartTime(readjson)

    start_data = datetime(
        year=data.year,
        month=data.month,
        day=data.day,
        hour=int(start_time[:start_time.find(':')]),
        minute=int(start_time[start_time.find(':')+1:start_time.rfind(':')]),
        second=int(start_time[start_time.rfind(':')+1:])
    )

    current_time_size = data-start_data
    current_minute = int(int(current_time_size.seconds)/60)
    current_seconds = int(current_time_size.seconds)%60

    if current_minute < 10:
        current_minute = f"0{current_minute}"
    
    if current_seconds < 10:
        current_seconds = f"0{current_seconds}"
    
    if endtime == 100:
        endtime = duration()
    else:
        endtime = newtime(duration(),endtime)

    if current_time_size.seconds != endtime:
        if music.get_busy():
            return False , f"{current_minute}:{current_seconds}"
        else:
            return False , "00:00"
    else:
        if music.get_busy():
            return True , f"{current_minute}:{current_seconds}"
        else:
            return False , "00:00"
"""

def current_time(type_ : str = 'time', controler : bool = False):
    if type_ == 'time':
        readjson_ = readjson()
        time_current_file = int(readjson_.GetCurrentTime())
        if not controler:
            sleep(0.8)
        if music.get_busy():
            readjson_.SetCurrentTime(str(time_current_file+1))

            minute = int(time_current_file/60)
            seconds = int(time_current_file%60)

            if minute < 10: minute = f"0{minute}"
            if seconds < 10: seconds = f"0{seconds}"

            return f"{minute}:{seconds}"
        else: return f"00:00"
    elif type_ == 'size':
        readjson_ = readjson()
        time_current_file = int(readjson_.GetCurrentTime())
        if not controler:
            sleep(0.8)
        if music.get_busy():
            readjson_.SetCurrentTime(str(time_current_file+1))
        return time_current_file
    else:
        return 0

        

