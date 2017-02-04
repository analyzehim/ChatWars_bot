import os

'''
def execute(exec_str):
    os.system('send-telegram.sh "{0}"'.format(exec_str))


exec_str = '/report'
# string = os.system('send-telegram.sh "{0}"'.format(exec_str))
string = os.popen('send-telegram.sh "{0}"'.format(exec_str)).read()


print '_______________'
print type(string)
print string

print 1
# string = os.popen('telegram-cli -k server.pub').read()

os.system('telegram-cli -k server.pub')
`
print 2
f = open("so1.txt","r")
for line in f:
	if 'Chat Wars' in line and 'Chat Wars' in line:
		print line
	print '_____'
f.close()


'''


import subprocess
import time

go_command = 'telegram-cli -W -e "msg MARK_I /go"'



def check_go():
	check_update = 'telegram-cli -W -e "quit"'
	result = subprocess.check_output(check_update, shell=True)
	for line in result.split('\n'):
		if 'Chat Wars' in line and '/go' in line:
			return True
	return False

while(True):
	if check_go():
		os.popen(go_command)
	time.sleep(2)


