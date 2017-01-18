import os
import time
import datetime

from const import *
from proto import *

f = open("castle.txt",'w')
f.write('white')
f.close()
castle = get_castle()
attack(castle)