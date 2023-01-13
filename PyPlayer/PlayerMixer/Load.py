from pygame.mixer import music
import os
from .filesTemp.Temp import temp
from .Play import play as  PLAY


class load():
    # ...
    # File = [path single file / path list file]
    def __init__(self,file=None,dir=None,loading : bool = False,play : bool = True,*args):
        if loading == False:
            if file != None:
                music.load(file)
                temp.InsertInFilesTemp(temp,file=file)
            elif dir != None:
                list_files = self.RuningPath(dir)
                file_ = temp.InsertInFilesTemp(temp,list_file=list_files)
                music.load(file_)
        else:
            self.LoadOtherFile(file=file,play=True)
    
    
    def RuningPath(self,dir):
        self.Files_MP3 = []
        # ...
        # Runing path and return all files of path
        files_of_path = os.listdir(dir)

        # Find all files mp3
        for file in files_of_path:
            extension_of_file = file.rfind('.')
            extension = file[extension_of_file+1:]
            if extension == 'mp3' or extension == 'MP3':
                self.Files_MP3.append(os.path.join(dir,file)) # Insert into list 'Files_MP3' a path of file
        
        return self.Files_MP3


    def LoadOtherFile(self,file=None,play=None):
        if play == True:
            music.load(file)
            PLAY()
        else:
            music.load(file)


