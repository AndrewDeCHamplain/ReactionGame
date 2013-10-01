#Client2
#importing socket to work with the server
import socket
#import the rest to use with the game
import time
import random
import piface.pfio as pfio

#setup the server's ip
hostname = '10.0.0.23'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 5050))
z = 0

#capture the cpu time of the raspberry pi as it starts
start_time = 0
time.sleep(2)

def game():
	global s
	global z
	toPress = random.randrange(0, 4, 1)	

	pfio.init()
	time.sleep(1)
	#time.sleep(1)
	#pfio.digital_write(0, 1)
	#pfio.digital_write(1, 1)
	#pfio.digital_write(2, 1)
	#time.sleep(1)
	#pfio.digital_write(2, 0)
	#time.sleep(1)
	#pfio.digital_write(1, 0)
	#time.sleep(1)
	#pfio.digital_write(0, 0)
	#time.sleep(1)

	start_time = time.clock()

	if(toPress == 0):
		pfio.digital_write(3, 1)

	elif(toPress == 1):
		pfio.digital_write(2, 1)

	elif(toPress == 2):
		pfio.digital_write(1, 1)

	else:
		pfio.digital_write(0, 1)
	
	#now that the keys and leds are setup, now to wait for the key to be pressed
	while(pfio.digital_read(toPress) == 0):
		pass
	#key pressed, grab the finish clock time
	end_time = time.clock()
	#subtract the 2 times to get the reaction time
	final_time = end_time - start_time
	#print ("Pressed in " + str(final_time) + " second(s) apparently.")
	

	#clear all the leds
	pfio.digital_write(0, 0)
	pfio.digital_write(1, 0)
	pfio.digital_write(2, 0)
	pfio.digital_write(3, 0)
	pfio.digital_write(4, 0)
	pfio.digital_write(5, 0)
	pfio.digital_write(6, 0)
	pfio.digital_write(7, 0)
	#send this reaction time
	send = int(final_time * 1000)
	#print str(send)
	s.send("'piface'" + str(send))
	#repeat 10 times in total to get an average
	if(z < 9):
		z = z + 1
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((hostname, 5050))
		game()




#start the game, by recieving start game from the server
while(z < 9):
	response = s.recv(1024)
	#print response
	if(response == 'start game'):
		game()

s.close()
