gameon = False
userinput = ""



def instructions()
    print "There are two raspberrypi's with peripheral boards attached. These function as controllers"
    print "This serverpi will send commands to them telling them which LEDs to light"        
    print "It will count the time it takes to react to each LED by pressing the correct button on the controller pi's"
    print "The winner will be determined by the lower average reaction time over 10 rounds"
    print "MOST IMPORTANTLY, HAVE FUN!"
    
    
def game()
    while (gameon):
        

def main()

    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "!!!!Welcome to Group B's RaspberryPi Reaction Time Game!!!!"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    while (gameon==False):
        print "Press Y to play, I for instructions, or Q to quit"
        userinput=getch()
        if (userinput=="i")
            instructions()
        if (userinput=="y")
            gameon=True
            game()
        if (userinput=="q")
            break        