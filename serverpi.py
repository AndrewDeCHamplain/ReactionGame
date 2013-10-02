#Group B making a simple server application
#involves networking and other experimental goodness

import socket
import re

pifaceround = 0
gertpiround = 0
pifacetotaltime = 0
gertpitotaltime = 0



def parsestring(stringin):
    global pifacetotaltime
    global gertpitotaltime
    global pifaceround
    global gertpiround
    
    r = re.match("^.*'(\w+)'(.*)$", stringin)          #parses incoming string from client pi
    if r:
        i,v = r.groups()
        if (i=="piface"):                              #determines which pi it came from
            pifacetotaltime=pifacetotaltime+int(v)          
            pifaceround=pifaceround+1
        elif (i=="gertpi"):
            gertpitotaltime=gertpitotaltime+int(v)
            gertpiround=gertpiround+1
        else:
            print "Invalid input recieved."


def instructions():
    print "\n\nThere are two raspberrypi's with peripheral boards attached. These function as controllers"
    print "This serverpi will send commands to them telling them which LEDs to light"        
    print "It will count the time it takes to react to each LED by pressing the correct button on the controller pi's"
    print "The winner will be determined by the lower average reaction time over 10 rounds"
    print "MOST IMPORTANTLY, HAVE FUN!\n"
    
    
##
# This is the part of the game which runs on the pi acting as server
# The server is in control of the game. It tells lets the clients know when to start the game.
# While the game is run client-side, the server receives the reaction time results
# and keeps track of the total. When it receives ten results, it calculates and displays an average.
##
def game():
    global pifacetotaltime
    global gertpitotaltime
    global pifaceround
    global gertpiround
    pifacetotaltime = 0
    gertpitotaltime = 0
    pifaceround = 0
    gertpiround = 0
       
    # Setting up this pi as a server using the socket library
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", 5050))                 #The server receives data from clients on port 5050
    s.listen(1)
    print "waiting for two players"
    komm, addr = s.accept()            #The server waits for the first client to connect                           
    komm2, addr = s.accept()	       #The server waits for the second client to connect
    raw_input("hit enter to start")    #The server is in control of the start of the game
    komm.send("start game")            #sends the start command to clients
    komm2.send("start game")                    
    while (True):
        parsestring(komm.recv(1024))   			    #Processes response from the first client
	parsestring(komm2.recv(1024))  			    #Processes response from second client (The order does not affect perceived results)
        if (pifaceround == 10 and gertpiround == 10):       #when round reaches 10, 10 responses have been received
            break                           	            #So we stop
        komm, addr = s.accept()                          #Wait for the clients to be ready to send another value
    piface_avg_time = pifacetotaltime/10.0              #Calculate the average time in milliseconds
    print "Piface average reaction time is: " + str(piface_avg_time) + " milliseconds"
    gertpi_avg_time = gertpitotaltime/10.0              #Calculate the average time in milliseconds
    print "Gertpi average reaction time is: " + str(gertpi_avg_time) + " milliseconds"
    
    print "Connection Terminated"      
    s.close()                          #End the program

def main():

    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "!!!!Welcome to Group B's RaspberryPi Reaction Time Game!!!!"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    while (True):
        userinput=raw_input("Press Y to play, I for instructions, or Q to quit: ")
        if (userinput=="i"):
            instructions()
        elif (userinput=="y"):
            game()
        elif (userinput=="q"):
            break
        else:
            print "Invalid Input"

main()
