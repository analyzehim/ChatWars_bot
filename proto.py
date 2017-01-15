import os
import time
import datetime
from const import *


def execute(exec_str):
    os.system('send-telegram.sh "{0}"'.format(exec_str))


def attackWhite():
    execute(attack_str)
    time.sleep(PAUSE)
    execute(white_str)


def attackBlue():
    execute(attack_str)
    time.sleep(PAUSE)
    execute(blue_str)


def forest():
    execute(quest_str)
    time.sleep(PAUSE)
    execute(forest_str)


def corovan():
    execute(quest_str)
    time.sleep(PAUSE)
    execute(corovan_str)


def ask_report():
    execute(report_str)


def defen():
    execute(defen_str)


def get_hour():
    return int(str(datetime.datetime.now()).split(' ')[1].split(':')[0])


def get_minute():
    return int(str(datetime.datetime.now()).split(' ')[1].split(':')[1])


def get_sec():
    return int(str(datetime.datetime.now()).split(' ')[1].split(':')[2].split('.')[0])


def get_time():
    return(get_hour(), get_minute(), get_sec())


def log_event(log_str):
    descr = open("log.txt", "a")
    print log_str
    descr.write(str(datetime.datetime.now())+' >>> ' + log_str + '\n')
    descr.close()
