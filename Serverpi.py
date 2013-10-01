#Group B making a simple server application
#involves networking and other experimental goodness

import socket
import re

userinput = ""
pifaceround = 0
gertpiround = 0
pifacetotaltime = 0
gertpitotaltime = 0



def parsestring(stringin):
    r = re.match("^.*'(\w+)'(.*)$", stringin)          #parses incoming string from client pi
    if r:
        i,v = r.groups()
        if (i=="piface"):                              #determines which pi it came from
            pifacetotaltime=pifacetotaltime+int(v)          #
            pifaceround=pifaceround+1
        elif (i=="gertpi"):
            gertpitotaltime=gertpitotaltime+int(v)
            gertpiround=gertpiround+1
        else:
            print "Invalid input recieved."


def instructions():
    print "There are two raspberrypi's with peripheral boards attached. These function as controllers"
    print "This serverpi will send commands to them telling them which LEDs to light"        
    print "It will count the time it takes to react to each LED by pressing the correct button on the controller pi's"
    print "The winner will be determined by the lower average reaction time over 10 rounds"
    print "MOST IMPORTANTLY, HAVE FUN!"
    
    
##
# This is the part of the game which runs on the pi acting as server
# The server is in control of the game. It tells lets the clients know when to start the game.
# While the game is run client-side, the server receives the reaction time results
# and keeps track of the total. When it receives ten results, it calculates and displays an average.
##
def game():
# Setting up this pi as a server using the socket library
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 5050))                 #The server receives data from clients on port 5050
s.listen(1)

komm, addr = s.accept()            #The server waits for the client to connect                       
data = raw_input("Enter Command: ")       #Once the connection is made, the server can start the game
if data == "stop":                        #Or it can quit
    pass
elif data == "start game":                #if the command is to start...
    round = 0                             #variable round keeps track of how many responses have been received
    total_time = 0                        #total_time stores the sum of reaction times
    komm.send(data)                       #sends the start command to clients
    while (True):
        end_time = komm.recv(1024)        #end_time is received from the client as a string type
        print "Waiting to receive response time..."
        print "received response in " + end_time + " milliseconds"               
        total_time = total_time + int(end_time)          #Sum the total time by changing the string end_time into an integer
        round += 1                                       #increment the round
        if round == 10:                     #when round reaches 10, 10 responses have been received
            break                           #So we stop
        komm, addr = s.accept()                          #Wait for the client to be ready to send another value
    avg_time = total_time/10.0              #Calculate the average time in milliseconds 
    print "Average reaction time is: " + str(avg_time) + " milliseconds"
else:
    print "invalid command"        #As of now only two commands are accepted: "start game" and "stop"
print "Connection Terminated"      
s.close()                          #End the program

def main():

    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "!!!!Welcome to Group B's RaspberryPi Reaction Time Game!!!!"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    while (True):
        print "Press Y to play, I for instructions, or Q to quit"
        userinput=getch()
        if (userinput=="i"):
            instructions()
        elif (userinput=="y"):
            game()
        elif (userinput=="q"):
            break
        else:
            print "Invalid Input"

