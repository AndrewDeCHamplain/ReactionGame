import RPi.GPIO as GPIO
import sys
import time
import random
import socket

GPIO.setwarnings(False)
board_type = sys.argv[-1]
hostname = '10.0.0.23'

if GPIO.RPI_REVISION == 1:      # check Pi Revision to set port 21/27 correctly
    # define ports list for Revision 1 Pi
    ports = [10, 9, 8, 7]
else:
    # define ports list all others
    ports = [10, 9, 8, 7]

ports_rev = ports[:]                            # make a copy of ports list

GPIO.setmode(GPIO.BCM)                  # initialise RPi.GPIO

for i in range(23,26):                  # set up ports 23-25
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # as inputs pull-ups high

for port_num in ports:
    GPIO.setup(port_num, GPIO.OUT)                  # set up ports for output

#print("Push correct button to turn off the LED.\n")
#raw_input("You will have 1 seconds once you're ready. When ready hit enter.\n")
#print("Starting in 3 seconds")
GPIO.output(7,0)
GPIO.output(8,0)
GPIO.output(9,0)
GPIO.output(10,0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 5050))

previous_status = ''
z = 0
x = 0

def game():
        global previous_status
        global x
	global s	
	global z

        time.sleep(1)
        starttime = time.clock()
        try:
                GPIO.output(7,0)
                GPIO.output(8,0)
                GPIO.output(9,0)
                ran = random.randrange(7,10)
                if (ran == 7):
                        random_list = ["0","0", "1"]
                        GPIO.output(7, 1)
                elif (ran == 8):
                        random_list = ["0","1", "0"]
                        GPIO.output(8, 1)
                else:
                        random_list = ["1", "0", "0"]
                        GPIO.output(9,1)

                while (x==0):
                        status_list = [GPIO.input(25), GPIO.input(24), GPIO.input(23)]
			for i in range(0,3):
				if status_list[i]:
					status_list[i] = "0"
				else:
					status_list[i] = "1"
                        if random_list == status_list:
                                for i in range(0,3):
                                        status_list[i] ="0"
                                #print("Correct!")
				GPIO.output(7,0)
				GPIO.output(8,0)
				GPIO.output(9,0)
                                endtime = time.clock()
                                finaltime = int((endtime - starttime) *1000)
                                #print "Took you " + str(finaltime) + ' milliseconds'
				#print("Next one in 1 second.\n")
                                s.send("'gertpi'" + str(finaltime))
				if (z<9):
					z = z + 1
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.connect((hostname, 5050))
					game()


        except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
                GPIO.cleanup()                 # resets all GPIO ports used by t$
        GPIO.cleanup()                     # on exit, reset all GPIO ports

while (z < 9):
	response = s.recv(1024)
	if (response == 'start game'):
		game()

s.close()

