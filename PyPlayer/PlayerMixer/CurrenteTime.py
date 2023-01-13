from mutagen.mp3 import MP3
from datetime import datetime
from .dbJson import readjson
from .Duration import duration

def currenttime():
    
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

    if f"{current_minute}:{current_seconds}" == duration():
        return 0
    else:
        return f"{current_minute}:{current_seconds}"
    
