import json as j
import os

class temp():

    def __init__(self):
        try:
            file = {
                "fileActive":"",
                "root_path":"",
                "fileslist":[]
            }
            time = {
                "current-time": "0",
                "file-time": "0",
                "play":False
            }
            with open(f"{os.getcwd()}\\cgs\\files.json",'w') as f:
                j.dump(file,f,indent=4,sort_keys=True)
            with open(f"{os.getcwd()}\\cgs\\time.json",'w') as f:
                j.dump(time,f,indent=4,sort_keys=True)
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Nenhuma pasta 'cgs' foi criada no seu diretório ráiz."
            )
    
    
    def InsertInFilesTemp(self,list_file=None,file=None):
        if list_file != None:
            self.FilesTempList(temp,list_file)
            return self.GetTempCurrenFile(temp)
        else:
            self.FilesTempFile(temp,file)
            return self.GetTempCurrenFile(temp)

    
    def FilesTempList(self,list_):
        try:
            with open(f"{os.getcwd()}/cgs/files.json") as f:
                text = f.read()
                file_dic = j.loads(text)
                file_dic["fileActive"] = f"{list_[0]}"
                file_dic["fileslist"] = list_

            with open(f"{os.getcwd()}/cgs/files.json",'w',encoding="utf-8") as f:
                j.dump(file_dic,f,indent=4,sort_keys=True)
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/files.json em seu diretório ráiz."
            )

    
    def FilesTempFile(self,file):
        try:
            with open(f"{os.getcwd()}/cgs/files.json") as f:
                text = f.read()
                file_dic = j.loads(text)

            file_dic["fileActive"] = f"{file}"
            file_dic["fileslist"] = file

            with open(f"{os.getcwd()}/cgs/files.json",'w',encoding="utf-8") as f:
                j.dump(file_dic,f,indent=4,sort_keys=True)
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/files.json em seu diretório ráiz."
            )

    
    def SetRootPath(self,file):
        try:
            with open(f"{os.getcwd()}/cgs/files.json") as f:
                text = f.read()
                file_dic = j.loads(text)
            file_dic["root_path"] = file

            with open(f"{os.getcwd()}/cgs/files.json",'w',encoding="utf-8") as f:
                j.dump(file_dic,f,indent=4,sort_keys=True)
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/files.json em seu diretório ráiz."
            )

    
    def ChangeCurrentFile(self,file):
        try:
            with open(f"{os.getcwd()}/cgs/files.json") as f:
                text = f.read()
                file_dic = j.loads(text)
                file_dic["fileActive"] = file

            with open(f"{os.getcwd()}/cgs/files.json",'w',encoding="utf-8") as f:
                j.dump(file_dic,f,indent=4,sort_keys=True)
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/files.json em seu diretório ráiz."
            )
    

    def GetRootPath(self):
        try:
            return_ = None
            with open(f"{os.getcwd()}/cgs/files.json",'r') as f:
                text = f.read()
                file_dic = j.loads(text)
                return_ = file_dic["root_path"]
            return return_
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/files.json em seu diretório ráiz."
            )

    
    def GetTempList(self):
        try:
            return_ = None
            with open(f"{os.getcwd()}/cgs/files.json",'r') as f:
                text = f.read()
                file_dic = j.loads(text)
                return_ = file_dic["fileslist"]
            return return_
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/files.json em seu diretório ráiz."
            )
    

    def GetTempCurrenFile(self):
        try:
            return_ = None
            with open(f"{os.getcwd()}/cgs/files.json",'r') as f:
                text = f.read()
                file_dic = j.loads(text)
                return_ = file_dic["fileActive"]
            return return_
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/files.json em seu diretório ráiz."
            )