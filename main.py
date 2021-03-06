from const import *
from proto import *
import random

def action(hour, minute):
    flag = False
    if hour in battle_hours:
        if minute == 5:
            time.sleep(random.randint(0, 20))
            ask_report()
            log_event('Ask report')
            flag = True

    if hour in [h - 1 for h in battle_hours]:
        if minute == 45:
            time.sleep(random.randint(0, 20))
            castle = get_castle()
            attack(castle)
            log_event('Attack {0}'.format(castle))
            flag = True

    if hour in cave_hours:
        if minute == 20:
            time.sleep(hour * 10)
            cave()
            log_event("Cave")
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
            time.sleep(60)

        except Exception as e:
            log_event(str(e))
