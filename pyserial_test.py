from textToMorse import TextToMorse
import serial
import string
try:
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
except Exception, e:
		ser=serial.Serial('COM3',9600,timeout=1)
while True:
	test=string.lower(raw_input('-->'))
	if test == ")":
		break
	ser.write(TextToMorse(test)+"\n")
ser.close()