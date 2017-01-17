import os
import time
import datetime

from const import *
from proto import *


def action(hour, minute):
    flag = False
    if hour in battle_hours:
        if minute == 5:
            ask_report()
            log_event('Ask report')
            flag = True

    if hour in [h - 1 for h in battle_hours]:
        if minute == 45:
            defen()
            log_event('Defen')
            flag = True

    if hour in corovan_hours:
        if minute in corovan_minutes:
            corovan()
            log_event("Corovan")
            flag = True

    if hour in cave_hours:
        if minute == 20:
            time.sleep(hour * 10)
            cave()
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
