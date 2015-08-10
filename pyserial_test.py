from textToMorse import function
import serial
import string
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
while True:
	test=string.lower(raw_input('-->'))
	if test == ")":
		break

#x = ser.read()          # read one byte
#s = ser.read(10)        # read #up to ten bytes (timeout)

#while True:
#thing="gasfg"
	ser.write(function(test)+"\n")
#line = ser.readline()
#print line
ser.close()
