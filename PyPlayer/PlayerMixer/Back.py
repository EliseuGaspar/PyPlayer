from .filesTemp.Temp import temp
from .Load import load

class back():
    def __init__(self,*args):
        current_file = temp.GetTempCurrenFile(temp)
        list_files = temp.GetTempList(temp)
        for x in range(len(list_files)):
            if list_files[x] == current_file:
                if x == 0:
                    load(file=list_files[len(list_files)-1],loading=True)
                    temp.ChangeCurrentFile(temp,list_files[len(list_files)-1])
                    break
                else:
                    load(file=list_files[x-1],loading=True)
                    temp.ChangeCurrentFile(temp,list_files[x-1])
                    break
    
    