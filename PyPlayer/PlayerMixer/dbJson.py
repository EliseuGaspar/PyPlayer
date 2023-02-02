import json as j
import os

class readjson():

    def __init__(self): pass

    def GetStartTime(self):
        try:
            with open(f"{os.getcwd()}/cgs/time.json") as db:
                content = db.read()
                content_json = j.loads(content)

            return content_json['start-time']
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/time.json em seu diretório ráiz."
            )
    
    def GetFileTime(self):
        try:
            with open(f"{os.getcwd()}/cgs/time.json") as db:
                content = db.read()
                content_json = j.loads(content)

            return content_json['file-time']
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/time.json em seu diretório ráiz."
            )
    
    def GetStatusTime(self):
        try:
            with open(f"{os.getcwd()}/cgs/time.json") as db:
                content = db.read()
                content_json = j.loads(content)

            return content_json['play']
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/time.json em seu diretório ráiz."
            )
    
    def GetCurrentTime(self):
        try:
            with open(f"{os.getcwd()}/cgs/time.json") as db:
                content = db.read()
                content_json = j.loads(content)

            return content_json['current-time']
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/time.json em seu diretório ráiz."
            )
    
    def SetStartTime(self,new_time:str):
        try:
            with open(f"{os.getcwd()}/cgs/time.json") as db:
                content = db.read()
                content_json = j.loads(content)
            
            content_json['start-time'] = new_time
            
            with open(f"{os.getcwd()}/cgs/time.json",'w') as db:
                j.dump(content_json,db,indent=4,sort_keys=True)
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/time.json em seu diretório ráiz."
            )
    
    def SetFileTime(self,new_time:str):
        try:
            with open(f"{os.getcwd()}/cgs/time.json") as db:
                content = db.read()
                content_json = j.loads(content)
            
            content_json['file-time'] = new_time
            
            with open(f"{os.getcwd()}/cgs/time.json",'w') as db:
                j.dump(content_json,db,indent=4,sort_keys=True)
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/time.json em seu diretório ráiz."
            )
    
    def SetCurrentTime(self,new_time:str):
        try:
            with open(f"{os.getcwd()}/cgs/time.json") as db:
                content = db.read()
                content_json = j.loads(content)
            
            content_json['current-time'] = new_time
            
            with open(f"{os.getcwd()}/cgs/time.json",'w') as db:
                j.dump(content_json,db,indent=4,sort_keys=True)
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/time.json em seu diretório ráiz."
            )

    def SetStatusTime(self,status : bool):
        try:
            with open(f"{os.getcwd()}/cgs/time.json") as db:
                content = db.read()
                content_json = j.loads(content)
            
            content_json['play'] = status
            
            with open(f"{os.getcwd()}/cgs/time.json",'w') as db:
                j.dump(content_json,db,indent=4,sort_keys=True)
        except FileNotFoundError:
            print(
                "PyPlayer.Error: Você precisa de um diretório cgs/time.json em seu diretório ráiz."
            )
    





