'''
skrf is an object-oriented approach to microwave engineering,
implemented in Python. 
'''
# Python 3 compatibility
from __future__ import absolute_import, print_function, division


__version__ = '0.16.1.dev'
## Import all  module names for coherent reference of name-space
#import io

from . import frequency
from . import network
from . import networkSet
from . import media

from . import calibration
from . import plotting
from . import mathFunctions
from . import tlineFunctions
from . import taper
from . import constants
from . import util
from . import io
from . import instances


# Import contents into current namespace for ease of calling
from .frequency import *
from .network import *
from .networkSet import *
from .calibration import *
from .util import *
from .plotting import  *
from .mathFunctions import *
from .tlineFunctions import *
from .io import * 
from .constants import * 
from .taper import * 
from .instances import * 

# Try to import vi, but if except if pyvisa not installed
try:
    import vi
    from vi import *
except(ImportError):
    pass

# try to import data but if it fails whatever. it fails if some pickles 
# dont unpickle. but its not important
try:
    from . import data
except:
    pass 



## built-in imports
from copy import deepcopy as copy


## Shorthand Names
F = Frequency
N = Network
NS = NetworkSet
lat = load_all_touchstones
saf  = save_all_figs

