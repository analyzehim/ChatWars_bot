import os
import time
import datetime

from const import *
from proto import *


def action(hour, minute):
    flag = False
    if minute == 10:
        if hour in battle_hours:
            ask_report()
            log_event('Ask report')
            flag = True

    if minute == 50:
        if hour in [h-1 for h in battle_hours]:
            defen()
            log_event('Defen')
            flag = True

    if (hour >= 4) and (hour < 7):
        if minute % 10 == 0:
            corovan()
            log_event("Corovan")
            flag = True

    if hour in forest_hours:
        if minute == 20:
            time.sleep(hour * 10)
            forest()
            log_event("Forest")
            flag = True
    return flag


def loop():
    (hour, minute, sec) = get_time()
    flag = action(hour, minute)
    if flag:
        print "Action on {0}:{1}:{2}".format(hour, minute, sec)
    else:
        print "No action on {0}:{1}:{2}".format(hour, minute, sec)


if __name__ == "__main__":
    while True:
        try:
            loop()
            time.sleep(40)

        except Exception as e:
            log_event(str(e))
