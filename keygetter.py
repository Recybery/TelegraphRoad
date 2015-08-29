import  pygame
import textToMorse
from pygame.locals import *
import time
import serial
import os

pygame.init()
screen = pygame.display.set_mode((700, 200))
pygame.display.set_caption('morse code!!')
fontobject = pygame.font.Font(None,50)
haveSer=True

di=0.1
da=3*di #from internet: dah=3 di's

L=""
autoreturn=0
try:
	ser = serial.Serial('Com3' if os.name=="nt" else '/dev/ttyACM0',
				9600, timeout=di)
except Exception, e:
		print "failed to set up serial for arduino"	
		print "but thats ok!! just use the 1 key on your keyboard or the mouse button!!"
		haveSer=False
def thing(s):
	print (s if s=="what" else "doh")
def readSer(gotten):
 	a=ser.read() # delays %timeout%(i.e. di) aeconds
	if(a=="+"): # "+" and "-" are symbols not handled by textToMorse.py so this program can't confuse
					#pyserial input from a keyboard and an arduino 
		gotten.append(pygame.event.Event(KEYDOWN,key=K_1))		
	elif(a=="_"):
		gotten.append(pygame.event.Event(KEYUP,key=K_1))
	return gotten

def screenPrint(s,b):
	screen.blit(fontobject.render(s, 10,(255,255,255)),(0,b))	
	pygame.display.flip()
def outPut(s):
	global L
	global autoreturn
	print s,
	L+=s
	autoreturn+=1
def  main():
	global L
	global autoreturn
	autospace=True
	slack=4 
	slashWhen=3+slack
	slashWhen2=7+(2*slack)# increases amount of time required for idle keyboard
		# or arduino to activate a slash compared to 
		# a dot or dash. i find it easier to enter cs that way
	if ~haveSer:
		clock = pygame.time.Clock()	
		freq=1/di
	pygame.key.set_repeat(1,1)## makes it so that holding down key creates events
	
	slash=0  #keeps track of cycles of loop for "/" printing/ concatenating
	down=False  #needed in conjuction w/pygeme.key.set_repeat() to keep line 75 from going when key held down
	#autoreturn =0 #when reaches a certain number prints "" automatically
	#L=""
	ultraBreak=False
	
	while not ultraBreak:

		screenPrint(L,80)
		gotten =  pygame.event.get()
		if haveSer :
			gotten =readSer(gotten)
		else:	
			clock.tick(freq)	
		if(autoreturn>=40):# may need to be adjusted per display or elimiated
			print ""
			autoreturn=0		
		if (gotten == [] and autospace and not pygame.mouse.get_pressed()[0]):
			if slash<=slashWhen2:
				slash+=1 
			if slash==slashWhen or slash== slashWhen2 :
					outPut("/")		
		else:
			
			slash=0
			for event in gotten:
				#print event
				#'''
				if event.type==MOUSEBUTTONDOWN:
					if(event.button==1):
						if down==False:
							down=True
							start = time.time()	
				#'''
				elif event.type==KEYDOWN:
					if event.key==K_TAB:
						autospace= not autospace
					elif  event.key==K_q:
						print event.key
						outPut(".")
					elif  event.key==K_w:
						outPut("-")
					elif event.key==K_PERIOD :
						outPut(".")
					elif event.key==K_MINUS:
						outPut("-")
					elif event.key==K_SLASH:
						outPut("/")
					elif event.key==K_2:
						outPut("/")
					
					elif event.key == K_1:
						if down==False:
							down=True
							start = time.time()				
					elif event.key == K_RETURN:
						print ""
						autoreturn=0
					elif event.key ==K_F1:
						print textToMorse.MorseToText(L)
						screen.fill((0,0,0))
						screenPrint(L,0)
						screenPrint(textToMorse.MorseToText(L),40)
						L=""
						autoreturn=0
					elif event.key ==K_ESCAPE:
						print ""
						ultraBreak=True		
					elif event.key==K_SPACE:
						outPut("/")
						outPut("/")
						slash=slashWhen2+1

				elif event.type == KEYUP and event.key == K_1:
					down=False
					end = time.time()
					if end-start>=da:
						outPut("-")
					else:
						outPut(".")
				elif event.type == QUIT:
					return
				elif event.type ==MOUSEBUTTONUP and event.button==1:
					down=False
					end = time.time()
					if end-start>=da:
						outPut("-")
					else:
						outPut(".")
				elif event.type ==MOUSEBUTTONUP and event.button==3:
					print textToMorse.MorseToText(L)
					screen.fill((0,0,0))
					screenPrint(L,0)
					screenPrint(textToMorse.MorseToText(L),40)
					L=""
					autoreturn=0
	return L

if __name__ == '__main__': a=main()
print textToMorse.MorseToText(a)
try:
	ser.close()
except Exception, e:
	pass
