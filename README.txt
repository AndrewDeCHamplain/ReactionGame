This is a project for SYSC3010 group b

It uses 3 networked raspberry pi's

one acts as a server and provides a gui, as well as tells the other PI's what to do

The other two pi's are effectively terminals that recieve data from the serverpi which tells them what LED to turn on

they count how long it takes the user to press the button that corresponds to the lit LED
they send that data back to the server pi

this process repeats till the game is over (user decision or 10 rounds)

the server then averages the 2 pi's overall reaction times

the winning pi's lights will all light up

end