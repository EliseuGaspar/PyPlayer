from mutagen.mp3 import MP3
from .filesTemp.Temp import temp
from .dbJson import readjson

def duration():
    current_file = MP3(temp.GetTempCurrenFile(temp))
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