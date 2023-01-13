from pygame import mixer

from .Load import load
from .Play import play
from .Pause import pause
from .UnPause import unpause
from .Stop import stop
from .Back import back
from .Next import next_
from .Volume import setvolume
from .Volume import getvolume
from .Repeat import repeat
from .CurrenteTime import currenttime
from .Duration import duration
from .Tag import tags


mixer.init()