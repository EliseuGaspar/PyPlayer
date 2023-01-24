from pygame.mixer import music
from .filesTemp.Temp import temp
from .Load import load
#from schedule import (every as e, repeat as r, run_pending as run)
from time import sleep


class repeat():
    
    def __init__(self,list_ : bool = True, file : bool = False, break_: bool = False):
        
        if file == True:
            self.repeat_file(break_ = break_)
        elif list_ == True:
            self.repeat_list(break_ = break_)
        else:
            pass
    
    def repeat_file(self, break_ : bool = False):
        pass

    def repeat_list(self, break_ : bool = False):
        pass


"""
@repeat(every(5).seconds)
def Atualizador_API():
    #print('Atualizando Câmbios')
    #Scraping_Banking()
    print('Atualizando Noticias')
    Scraping_News()


while True:
    run_pending()
    sleep(1)
    print(p)
    p+=1
"""