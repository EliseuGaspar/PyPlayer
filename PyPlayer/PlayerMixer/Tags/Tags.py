from mutagen.mp3 import MP3
import mutagen
from ..filesTemp.Temp import temp


class tags():

    def __init__(self):
        pass

    def full():
        current_file = temp.GetTempCurrenFile(temp)
        audio = mutagen.File(current_file)
        try:
            track = audio['TRCK'].text[0]
            album = audio['TALB'].text[0]
            title = audio['TIT2'].text[0]
            artist = audio['TPE2'].text[0]
            genero = audio['TCON'].text[0]
            year = audio['TDRC'].text[0]
        except:
            track = "Unknown"
            album = "Unknown"
            title = "Unknown"
            artist = "Unknown"
            genero = "Unknown"
            year = "Unknown"

        return {
            "Artist":artist,
            "Title":title,
            "Album":album,
            "Faixa":track,
            "Genero":genero,
            "Ano":year
        }

    def title(self):
        current_file = temp.GetTempCurrenFile(temp)
        audio = mutagen.File(current_file)
        
        try:
            title = audio['TIT2'].text[0]
        except:
            title = "Unknown"

        return title

    def artist(self):
        current_file = temp.GetTempCurrenFile(temp)
        audio = mutagen.File(current_file)
        try:
            artist = audio['TPE2'].text[0]
        except:
            artist = "Unknown"

        return artist

    def album(self):
        current_file = temp.GetTempCurrenFile(temp)
        audio = mutagen.File(current_file)
        try:
            album = audio['TALB'].text[0]
        except:
            album = "Unknown"

        return album


