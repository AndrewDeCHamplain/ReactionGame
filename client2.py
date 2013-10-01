import socket

import time
import random
import piface.pfio as pfio

hostname = '10.0.0.23'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 5050))
x = 0
	#send = raw_input('Enter something: ')
	#s.send(send)                #achnowledge connection, send hello world
	

start_time = 0

def game():
   global s
   y = 0
   while(y == 0):
	toPress = random.randrange(0, 4, 1)
	
	y = 0

	pfio.init()
	time.sleep(1)
	pfio.digital_write(0, 1)
	pfio.digital_write(1, 1)
	pfio.digital_write(2, 1)
	time.sleep(1)
	pfio.digital_write(2, 0)
	time.sleep(1)
	pfio.digital_write(1, 0)
	time.sleep(1)
	pfio.digital_write(0, 0)
	time.sleep(1)

	con_time = time.clock()
	#start_time = 0

	#pfio.digital_write(toPress, 1)
	if(toPress == 0):
		pfio.digital_write(3, 1)
		pfio.digital_write(7, 1)
	elif(toPress == 1):
		pfio.digital_write(2, 1)
		pfio.digital_write(6, 1)
	elif(toPress == 2):
		pfio.digital_write(1, 1)
		pfio.digital_write(5, 1)
	else:
		pfio.digital_write(0, 1)
		pfio.digital_write(4, 1)

	#pfio.digital_write((toPress *2), 1)

	while(pfio.digital_read(toPress) == 0):
		#start_time = start_time +1
		#time.sleep(1)
		y = y + 1
	#print ("Clock time is " + str(start_time) + " second(s).")
#	end_time = time.clock()
#	final_time = float(end_time) - float(start_time)
#	start_time = int(end_time)
#	print ("Pressed in " + str(final_time) + " second(s) apparently.")
	

	
	pfio.digital_write(0, 0)
	pfio.digital_write(1, 0)
	pfio.digital_write(2, 0)
	pfio.digital_write(3, 0)
	pfio.digital_write(4, 0)
	pfio.digital_write(5, 0)
	pfio.digital_write(6, 0)
	pfio.digital_write(7, 0)

	s.send("done")
	break






while(x == 0):
	response = s.recv(1024)      #recieve packets *i think*
	print response
	if(response == 'start game'):
		game()

s.close()
