#Group B making a simple server application
#involves networking and other experimental goodness

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 5050))
s.listen(1)
x = 0
while(x == 0):
	komm, addr = s.accept()
	data = raw_input("Enter Command: ")
	if data == "stop":
		x = 1
	elif data == "start game":
		y = 0
		total_time = 0
		komm.send(data)
		while (0 == 0):
			end_time = komm.recv(1024)
			print "Waiting to receive response time..."
			print "received response in " + end_time + " milliseconds"
			total_time = total_time + int(end_time)
			y += 1
			if y == 10:
				break
			komm, addr = s.accept()
		avg_time = total_time/10.0
		print "Average reaction time is: " + str(avg_time) + " milliseconds"
	else:
		print "invalid command"
 	x = 1
print "Connection Terminated"
s.close()

