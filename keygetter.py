import os, pygame
import textToMorse
from pygame.locals import *
import time
import serial

pygame.init()
screen = pygame.display.set_mode((700, 200))
pygame.display.set_caption('morse code!!')
fontobject = pygame.font.Font(None,50)
white=(255,255,255)
haveSer=True
di=0.1 #length seconds of a '.' i.e di in morse
da=3*di #from internet: dah=3 di's
slack=4 # increases amount of time required for idle keyboard
		# or arduino to activate a slash compared to the
		# a dot or dash
try:
	ser = serial.Serial(
				'COM3',
				9600, timeout=di)
except Exception, e:
	try:
		ser = serial.Serial(
				'/dev/ttyACM0',#maybe different per machine
				9600, timeout=di)
	except Exception, e:
			print "failed to set up serial"	
			print "but thats ok!! just use the 1 key on your keyboard!!"
			haveSer=False
def readSer(gotten):
	#c=time.time()
 	a=ser.read()
 	#print time.time()-c 
	if(a=="+"): # "+" and "-" are symbols not handled by textToMorse.py so this program can't confuse
					#pyserial input from a keyboard and an arduino 
		gotten.append(pygame.event.Event(KEYDOWN,key=K_1))		
	elif(a=="_"):
		gotten.append(pygame.event.Event(KEYUP,key=K_1))
	return gotten

def screenPrint(s,b):
	screen.blit(fontobject.render(s, 10,white),(0,b))	
	pygame.display.flip()
def  main():

	clock = pygame.time.Clock()	
	pygame.key.set_repeat(1,1)## makes it so that holding down key creates events
	
	slash=0  #keeps track of cycles of loop for "/" printing/ concatenating
	down=False  #needed in conjuction w/pygeme.key.set_repeat() to keep line 75 from going when key held down
	autoreturn =0 #when reaches a certain number prints "" automatically
	ultraBreak=False
	L=""
	while not ultraBreak:

		#clock.tick(3)
		screenPrint(L,0)

		gotten =  pygame.event.get()
		if haveSer :
			gotten =readSer(gotten)
		else:	
			clock.tick(1/(di))	
		if(autoreturn>=40):# may need to be adjusted per display or elimiated
			print ""
			autoreturn=0		
		if (gotten == [] ):
			if slash<=7+(2*slack):
				slash+=1 
			if slash==3+slack :
					#slash=0
				print "/",
				L+="/"
				autoreturn+=1
			if slash ==7+(2*slack):#from internet :space between words =7 di's
				print "/",
				L+="/"
				autoreturn+=1			#stops printing slash after 2
		else:
			slash=0
			for event in gotten:
				#if event.type==KEYUP:
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN and event.key == K_1:
					if down==False:
						down=True
						start = time.time()
				elif event.type == KEYUP and event.key == K_1:
					down=False
					end = time.time()
					if end-start>=da: #from internet: dash =3 di's
						print "-",
						L+="-"
						autoreturn+=1
					else:
						print ".",
						L+="."
						autoreturn+=1
				elif event.type == KEYDOWN and event.key == K_RETURN:
					print ""
					autoreturn=0
				elif event.type == KEYDOWN and event.key ==K_F1:
					screenPrint(textToMorse.MorseToText(L),20)
				elif event.type == KEYDOWN and event.key ==K_ESCAPE:
					print ""
					ultraBreak=True		
				elif event.type== KEYDOWN and event.key==K_SPACE:
					print "//",
					L+="//"
				elif event.type==KEYDOWN and event.key==K_F2:
					print textToMorse.MorseToText(L)
					L=""
					autoreturn=0
    	pygame.display.flip()
    	
	return L

#this calls the 'main' function when this script is executed
if __name__ == '__main__': a=main()
print textToMorse.MorseToText(a)
try:
	ser.close()
except Exception, e:
	pass
