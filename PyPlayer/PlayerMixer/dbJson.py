import json as j

class readjson():

    def __init__(self): pass

    def GetStartTime(self):
        with open('PyPlayer\\PlayerMixer\\db.json') as db:
            content = db.read()
            content_json = j.loads(content)

        return content_json['start-time']
    
    def GetFileTime(self):
        with open('PyPlayer\\PlayerMixer\\db.json') as db:
            content = db.read()
            content_json = j.loads(content)

        return content_json['file-time']
    
    def SetStartTime(self,new_time:str):
        """
        new_time = [str(hour,minute,second)]
        """
        with open('PyPlayer\\PlayerMixer\\db.json') as db:
            content = db.read()
            content_json = j.loads(content)
        
        content_json['start-time'] = new_time
        
        with open('PyPlayer\\PlayerMixer\\db.json','w') as db:
            j.dump(content_json,db,indent=4,sort_keys=True)
    
    def SetFileTime(self,new_time:str):
        """
        new_time = [str(minute,second)]
        """
        with open('PyPlayer\\PlayerMixer\\db.json') as db:
            content = db.read()
            content_json = j.loads(content)
        
        content_json['file-time'] = new_time
        
        with open('PyPlayer\\PlayerMixer\\db.json','w') as db:
            j.dump(content_json,db,indent=4,sort_keys=True)