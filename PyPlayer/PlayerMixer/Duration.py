from mutagen.mp3 import MP3
from .filesTemp.Temp import temp
from .dbJson import readjson

def duration(type_ : str = 'time'):
    if type_ == 'time':
        file = temp.GetTempCurrenFile(temp)
        current_file = MP3(file)
        readjson.SetFileTime(
            readjson,
            f"{(int(current_file.info.length/60)*60)+(int(current_file.info.length%60)+4)}"
        )

        minute = int(current_file.info.length/60)
        second = (int(current_file.info.length%60)+4)

        if minute < 10:
            minute = f"0{minute}"
        
        if second < 10:
            second = f"0{second}"

        return f"{minute}:{second}"
    elif type_ == 'size':
        file = temp.GetTempCurrenFile(temp)
        current_file = MP3(file)
        return current_file.info.length
    else:
        return False