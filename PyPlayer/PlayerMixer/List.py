from .filesTemp.Temp import temp
import sys


def list_():
    try:
        list_files = []
        files = temp.GetTempList(temp)
        if type(files) == list:
            for x in files:
                x = x[x.rfind('/')+1:]
                list_files.append(x)
            return list_files
        else:
            files = files[files.rfind('/')+1:]
            files = files[files.rfind('\\')+1:]
            list_files.append(files)
            return list_files
    except: pass

def current_file():
    try:
        file = temp.GetTempCurrenFile(temp)
        file = file[file.rfind('/')+1:len(file)]
        return file
    except: pass