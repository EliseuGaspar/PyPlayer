import json as j
import os

class readjson():

    def __init__(self): 
        pass

    def GetStartTime(self):
        with open(f"{os.getcwd()}/PyConfigs/db.json") as db:
            content = db.read()
            content_json = j.loads(content)

        return content_json['start-time']
    
    def GetFileTime(self):
        with open(f"{os.getcwd()}/PyConfigs/db.json") as db:
            content = db.read()
            content_json = j.loads(content)

        return content_json['file-time']
    
    def GetCurrentTime(self):
        with open(f"{os.getcwd()}/PyConfigs/db.json") as db:
            content = db.read()
            content_json = j.loads(content)

        return content_json['current-time']
    
    def SetStartTime(self,new_time:str):
        with open(f"{os.getcwd()}/PyConfigs/db.json") as db:
            content = db.read()
            content_json = j.loads(content)
        
        content_json['start-time'] = new_time
        
        with open(f"{os.getcwd()}/PyConfigs/db.json",'w') as db:
            j.dump(content_json,db,indent=4,sort_keys=True)
    
    def SetFileTime(self,new_time:str):
        with open(f"{os.getcwd()}/PyConfigs/db.json") as db:
            content = db.read()
            content_json = j.loads(content)
        
        content_json['file-time'] = new_time
        
        with open(f"{os.getcwd()}/PyConfigs/db.json",'w') as db:
            j.dump(content_json,db,indent=4,sort_keys=True)
    
    def SetCurrentTime(self,new_time:str):
        with open(f"{os.getcwd()}/PyConfigs/db.json") as db:
            content = db.read()
            content_json = j.loads(content)
        
        content_json['current-time'] = new_time
        
        with open(f"{os.getcwd()}/PyConfigs/db.json",'w') as db:
            j.dump(content_json,db,indent=4,sort_keys=True)






