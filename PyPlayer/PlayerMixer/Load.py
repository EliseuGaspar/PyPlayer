import pygame
from pygame.mixer import music
import os
from .filesTemp.Temp import temp
from .Play import play as  PLAY


class load():
    # ...
    # File = [path single file / path list file]
    def __init__(self , file : str = None , dir : str = None,
    list_ : list = None , loading : bool = False , *args):

        if loading != False and file != None:
            self.LoadOtherFile(file=file,play=True)
        else:
            if file != None:
                try:
                    music.load(file)
                except pygame.error:
                    print(
                        f"PyPlayer.Error: O caminho introduzido não existe ou o arquivo {file} está corrompido"
                    )
                temp.InsertInFilesTemp(temp,file=file)
            elif dir != None:
                list_files = self.RuningPath(dir)
                file_ = temp.InsertInFilesTemp(temp,list_file=list_files)
                try:
                    music.load(file_)
                except pygame.error:
                    print(
                        f"PyPlayer.Error: O caminho introduzido não existe ou o arquivo {file_} está corrompido"
                    )
            elif list_ != None:
                file_ = temp.InsertInFilesTemp(temp,list_file=list_)
                try:
                    music.load(file_)
                except pygame.error:
                    print(
                        f"PyPlayer.Error: O caminho introduzido não existe ou o arquivo {file_} está corrompido"
                    )
    
    
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
            try:
                music.load(file)
            except pygame.error:
                print(
                    f"PyPlayer.Error: O caminho introduzido não existe ou o arquivo {file} está corrompido"
                )
            PLAY()
        else:
            try:
                music.load(file)
            except pygame.error:
                print(
                    f"PyPlayer.Error: O caminho introduzido não existe ou o arquivo {file} está corrompido"
                )



