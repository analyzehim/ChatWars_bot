import os
import time
import datetime

f = open('symbols/quest','r')
for quest_str in f:
	break
f.close()

f = open('symbols/forest','r')
for forest_str in f:
	break
f.close()

f = open('symbols/corovan','r')
for corovan_str in f:
	break
f.close()

f = open('symbols/defen','r')
for defen_str in f:
	break
f.close()

f = open('symbols/attack','r')
for attack_str in f:
	break
f.close()

f = open('symbols/white','r')
for white_str in f:
	break
f.close()

report_str ='/report'

def execute(exec_str):
	os.system('send-telegram.sh "{0}"'.format(exec_str))

def attackWhite():
	execute(attack_str)
	time.sleep(5)
	execute(white_str)

def forest():
	execute(quest_str)
	time.sleep(10)
	execute(forest_str)

def corovan():
	execute(quest_str)
	time.sleep(10)
	execute(corovan_str)

def ask_report():
	execute(report_str)

def defen():
	execute(defen_str)

def get_hour():
	return int(str(datetime.datetime.now()).split(' ')[1].split(':')[0])


def log_event(log_str):
	f = open("log.txt","a")
	print log_str
	f.write(str(datetime.datetime.now())+' >>> ' + log_str + '\n')
	f.close()


def loop():

	log_event('_____Begin of loop_____')
	try:

			
		if (get_hour() >= 2) and (get_hour() <= 9):
			corovan()
			time.sleep(320)
			log_event("Night corovan, sleep 320")

		elif (get_hour() >=9) and (get_hour() <=14):
			forest()
			time.sleep(320)
			log_event("Non-night forest, sleep 320")
		else:
			log_event("too son, {0}".format(get_hour()))
		defen()
		log_event('Normal defen')

	except Exception as e:
		log_event(str(e))


		defen()
		log_event("Error defen")

	log_event('sleep 30 min')	
	time.sleep(1800)

timestamp = time.time()
ask_report()
while True:
	try:
		loop()
		
		if time.time() - timestamp >= 9000:
			timestamp = time.tme()
			ask_report()
			log_event('Ask report')

	except Exception as e:
		log_event(str(e))
		break

