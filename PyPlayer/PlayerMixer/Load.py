import pygame
from pygame.mixer import music
import os
from .filesTemp.Temp import temp
from .Play import play as  PLAY




def load(file : str = None , dir : str = None,
    list_ : list = None , loading : bool = False , *args):

    def RuningPath(dir):
        Files_MP3 = []

        files_of_path = os.listdir(dir)

        for file in files_of_path:
            extension_of_file = file.rfind('.')
            extension = file[extension_of_file+1:]
            if extension == 'mp3' or extension == 'MP3':
                Files_MP3.append(f"{dir}/{file}")
        
        return Files_MP3
    
    def LoadOtherFile(file=None):
        try:
            music.load(file)
            temp.ChangeCurrentFile(temp,file)
        except pygame.error:
            print(
                f"PyPlayer.Error: O caminho introduzido não existe ou o arquivo {file} está corrompido"
            )
        PLAY()
    
    def InsertPath():
        try:
            file = temp.GetTempCurrenFile(temp)
            file = file[:file.rfind('/')+1]
            temp.SetRootPath(temp,file)
        except: pass
    
    if loading != False and file != None:
        LoadOtherFile(file=file)
    else:
        if file != None:
            try:
                music.load(file)
            except pygame.error:
                print(
                    f"PyPlayer.Error: O caminho introduzido não existe ou o arquivo {file} está corrompido"
                )
            temp.InsertInFilesTemp(temp,file=file)
            InsertPath()
        elif dir != None:
            list_files = RuningPath(dir)
            if list_files == []:
                return False
            else:
                file_ = temp.InsertInFilesTemp(temp,list_file=list_files)
                try:
                    music.load(file_)
                    InsertPath()
                except pygame.error:
                    print(
                        f"PyPlayer.Error: O caminho introduzido não existe ou o arquivo {file_} está corrompido"
                    )
        elif list_ != None:
            file_ = temp.InsertInFilesTemp(temp,list_file=list_)
            try:
                music.load(file_)
                InsertPath()
            except pygame.error:
                print(
                    f"PyPlayer.Error: O caminho introduzido não existe ou o arquivo {file_} está corrompido"
                )
