from pygame import mixer
import os

from .Load import load
from .Play import play
from .Pause import pause
from .UnPause import unpause
from .Stop import stop
from .Back import back
from .Next import next_
from .Volume import setvolume
from .Volume import getvolume
from .Restart import restart
from .CurrenteTime import currenttime, current_time
from .Duration import duration
from .List import list_ , current_file
from .Tag import tags
from .SetTime import settime
from .Playing import playing
from .___Init___ import ___init___

___init___()
mixer.init()
