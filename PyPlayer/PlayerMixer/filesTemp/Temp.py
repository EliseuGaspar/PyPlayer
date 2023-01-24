import json as j
import os

class temp():

    def __init__(self):
        file_dic = {
            "fileActive":"",
            "fileslist":[]
        }
        file_db = {
            "current-time": "",
            "file-time": "",
            "start-time": ""
        }
        with open(f"{os.getcwd()}/PyConfigs/files.json",'w') as f:
            j.dump(file_dic,f,indent=4,sort_keys=True)
        with open(f"{os.getcwd()}/PyConfigs/db.json",'w') as f:
            j.dump(file_db,f,indent=4,sort_keys=True)

    
    def InsertInFilesTemp(self,list_file=None,file=None):
        if list_file != None:
            self.FilesTempList(temp,list_file)
            return self.GetTempCurrenFile(temp)
        else:
            self.FilesTempFile(temp,file)
            return self.GetTempCurrenFile(temp)

    
    def FilesTempList(self,list_):
        with open(f"{os.getcwd()}/PyConfigs/files.json") as f:
            text = f.read()
            file_dic = j.loads(text)
            file_dic["fileActive"] = f"{list_[0]}"
            file_dic["fileslist"] = list_

        with open(f"{os.getcwd()}/PyConfigs/files.json",'w',encoding="utf-8") as f:
            j.dump(file_dic,f,indent=4,sort_keys=True)

    
    def FilesTempFile(self,file):
        with open(f"{os.getcwd()}/PyConfigs/files.json") as f:
            text = f.read()
            file_dic = j.loads(text)

        file_dic["fileActive"] = f"{file}"
        file_dic["fileslist"] = file

        with open(f"{os.getcwd()}/PyConfigs/files.json",'w',encoding="utf-8") as f:
            j.dump(file_dic,f,indent=4,sort_keys=True)
    

    def ChangeCurrentFile(self,file):
        with open(f"{os.getcwd()}/PyConfigs/files.json") as f:
            text = f.read()
            file_dic = j.loads(text)
            file_dic["fileActive"] = file

        with open(f"{os.getcwd()}/PyConfigs/files.json",'w',encoding="utf-8") as f:
            j.dump(file_dic,f,indent=4,sort_keys=True)

    
    def GetTempList(self):
        return_ = None
        with open(f"{os.getcwd()}/PyConfigs/files.json",'r') as f:
            text = f.read()
            file_dic = j.loads(text)
            return_ = file_dic["fileslist"]
        return return_
    

    def GetTempCurrenFile(self):
        return_ = None
        with open(f"{os.getcwd()}/PyConfigs/files.json",'r') as f:
            text = f.read()
            file_dic = j.loads(text)
            return_ = file_dic["fileActive"]
        return return_