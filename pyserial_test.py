from textToMorse import TextToMorse
import serial
import string
ser = serial.Serial('\COM3', 9600, timeout=1)
while True:
	print ser.read()
ser.close()
