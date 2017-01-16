import os
import time
import datetime

from const import *
from proto import *


def action(hour, minute):
    flag = False
    if minute == 5:
        if hour in battle_hours:
            ask_report()
            log_event('Ask report')
            flag = True

    elif minute == 45:
        if hour in [h-1 for h in battle_hours]:
            defen()
            log_event('Defen')
            flag = True

    elif minute in corovan_minutes:
        if hour in corovan_hours:
            corovan()
            log_event("Corovan")
            flag = True

    elif minute == 20:
        if hour in forest_hours:
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
