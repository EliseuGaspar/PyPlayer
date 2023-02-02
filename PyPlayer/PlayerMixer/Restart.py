from .filesTemp.Temp import temp
from .Load import load

class restart():
    def __init__(self):
        list_files = temp.GetTempList(temp)
        temp.ChangeCurrentFile(temp,list_files[0])
        load(file=list_files[0],loading=True)