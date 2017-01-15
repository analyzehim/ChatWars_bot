import os
import time
import datetime

from const import *
from proto import *


def action(hour, minute):
    if minute == 10:
        if hour in battle_hours:
            ask_report()
            log_event('Ask report')

    if minute == 50:
        if hour in [h-1 for h in battle_hours]:
            defen()
            log_event('Defen')

    if (hour >= 4) and (hour < 7):
        if minute % 10 == 0:
            corovan()
            log_event("Corovan")

    if hour in forest_hours:
        if minute == 20:
            time.sleep(hour * 10)
            forest()
            log_event("Forest")


def loop():
    (hour, minute) = get_time()
    action(hour, minute)
    time.sleep(40)


if __name__ == "__main__":
    while True:
        try:
            loop()

        except Exception as e:
            log_event(str(e))


