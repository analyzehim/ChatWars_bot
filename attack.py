import os
import time
import datetime

from const import *
from proto import *
castle = raw_input()
f = open("castle.txt", 'w')
f.write(castle)
f.close()
castle = get_castle()
attack(castle)
