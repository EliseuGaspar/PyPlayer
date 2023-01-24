from .filesTemp.Temp import temp
import sys


def list_():
    list_files = []
    files = temp.GetTempList(temp)
    for x in files:
        if sys.platform != 'win32':
            x = x[x.rfind('/')+1:]
        else:
            x = x[x.rfind('\\')+1:]
        list_files.append(x)
    return list_files


def current_file():
    file = temp.GetTempCurrenFile(temp)
    if sys.platform == 'win32': 
        file = file[file.rfind('\\')+1:len(file)]
    if sys.platform != 'win32':
        file = file[file.rfind('/')+1:len(file)]
    return file