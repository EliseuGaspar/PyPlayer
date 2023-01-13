import json as j
import os

class temp():

    def __init__(self):
        pass

    
    def InsertInFilesTemp(self,list_file=None,file=None):
        if list_file != None:
            self.FilesTempList(self,list_file)
            return self.GetTempCurrenFile(self)
        else:
            self.FilesTempFile(self,file)
            return self.GetTempCurrenFile(self)

    
    def FilesTempList(self,list_):
        with open('PyPlayer\PlayerMixer\\filesTemp\\files.json') as f:
            text = f.read()
            file_dic = j.loads(text)
            file_dic["fileActive"] = f"{list_[0]}"
            file_dic["fileslist"] = list_

        with open('PyPlayer\PlayerMixer\\filesTemp\\files.json','w') as f:
            j.dump(file_dic,f,indent=4,sort_keys=True)

    
    def FilesTempFile(self,file):
        with open('PyPlayer\PlayerMixer\\filesTemp\\files.json') as f:
            text = f.read()
            file_dic = j.loads(text)

        file_dic["fileActive"] = f"{file}"
        file_dic["fileslist"] = file

        with open('PyPlayer\PlayerMixer\\filesTemp\\files.json','w') as f:
            j.dump(file_dic,f,indent=4,sort_keys=True)
    

    def ChangeCurrentFile(self,file):
        with open('PyPlayer\PlayerMixer\\filesTemp\\files.json') as f:
            text = f.read()
            file_dic = j.loads(text)
            file_dic["fileActive"] = file

        with open('PyPlayer\PlayerMixer\\filesTemp\\files.json','w') as f:
            j.dump(file_dic,f,indent=4,sort_keys=True)

    
    def GetTempList(self):
        return_ = None
        with open('PyPlayer\PlayerMixer\\filesTemp\\files.json','r') as f:
            text = f.read()
            file_dic = j.loads(text)
            return_ = file_dic["fileslist"]
        return return_
    

    def GetTempCurrenFile(self):
        return_ = None
        with open('PyPlayer\PlayerMixer\\filesTemp\\files.json','r') as f:
            text = f.read()
            file_dic = j.loads(text)
            return_ = file_dic["fileActive"]
        return return_