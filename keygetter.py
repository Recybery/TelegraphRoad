#/usr/bin/env python

#Import Modules
import os, pygame
import textToMorse
from pygame.locals import *
import time
import serial


#functions to create our resources
#TODO:as;ldkfj
#classes for our game objects
'''
#TODO:  comment line 27 and 57: I don't have an arduino can't test it
		Code with some work should reverse last weeks program!
'''
pygame.init()
screen = pygame.display.set_mode((700, 200))
pygame.display.set_caption('morse code!!')
pygame.display.flip()
fontobject = pygame.font.Font(None,50)
white=(255,255,255)
di=0.1 #length seconds of a '.' i.e di in morse
da=3*di #from internet: dah=3 di's
def  main():
	''' #this is line 27
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	ser.write(str(di*1000))+"\n")   #trys to synchronizes speed of python and pyserial
	#'''							#arduino di in milliseconds, python in seconds
#Initialize Everything
	L=""
#Prepare Game Objects
	clock = pygame.time.Clock()

	
	pygame.key.set_repeat(1,1)## makes it so that holding down key creates events
	slash=0 #keeps track of cycles of loop for "/" printing/ concatenating
	down=False #needed in conjuction w/pygeme.key.set_repeat() to keep line 75 from going when key held down
	autoreturn=0 #when reaches a certain number prints "" automatically
	
	
	
	 #creates string of {/.-}'s to be translated into text
	ultraBreak=False
	#Main Loop
	while not ultraBreak:
		screen.blit(fontobject.render(L, 0,white
								),
				(0, 0))
		pygame.display.flip()
		pygame.display.update()
	
		#delays loop so doesn't go too fast
		clock.tick(1/(di))
		gotten =  pygame.event.get()
		'''#this is line 57
		a=ser.readline()
		if(a=="+"): # "+" and "-" are symbols not handled by textToMorse.py so this program can't confuse
					#pyserial input from a keyboard and an arduino 
			gotten.append(pygame.event.Event(KEYDOWN,key=K_1))		
		elif(a=="-"):
			gotten.append(pygame.event.Event(KEYUP,key=K_1))	
		#'''
    	# like I said in my overly long git commit message, delays 1/speed (di)seconds
    	#Handle Input Events
		
		#print gotten, type(gotten)
		#print space
		if(autoreturn>=55):# may need to be adjusted per display or elimiated
			print ""
			autoreturn=0		
		if (gotten == [] ):
			if slash<=7:
				slash=slash+1 
			if slash==3 : #from internet :space between letters =3 di's
				#slash=0
				print "/",
				L+="/"
				autoreturn+=1
			if slash ==7:#from internet :space between words =7 di's
				print "/",
				L+="/"
				autoreturn+=1
			#stops printing slash after 2
		else:
			slash=0
			for event in gotten:
				#if event.type==KEYUP:
				
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN and event.key == K_1:
					#print "PING"
					#print gotten
					if down==False:
						down=True
						start = time.time()
						#print start
						#print down
				elif event.type == KEYUP and event.key == K_1:
					down=False
					end = time.time()
					if end-start>da: #from internet: dash =3 di's
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
					screen.blit(fontobject.render(textToMorse.MorseToText(L), 10,(255,255,255)#(255,255,255)
								),
				(0, 30))
				elif event.type == KEYDOWN and event.key ==K_ESCAPE:
					print ""
					ultraBreak=True
					
				elif event.type== KEYDOWN and event.key==K_SPACE:
					print "/ /",
					L+="/ /"
    #Draw Everything
    
        #pygame.display.flip()
        
#Game Over
	
	return L

#this calls the 'main' function when this script is executed
if __name__ == '__main__': a= main()
print textToMorse.MorseToText(a)

