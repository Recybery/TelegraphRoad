

#/usr/bin/env python

"""
This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation, 
follow along in the tutorial.
"""


#Import Modules
import os, pygame
import textToMorse
from pygame.locals import *
import time


#functions to create our resources

#classes for our game objects
def  main():
	"""this function is called when the program starts.
		it initializes everything it needs, then runs in
		a loop until the function returns."""
#Initialize Everything
	pygame.init()
	screen = pygame.display.set_mode((468, 60))
	#pygame.display.set_caption('Monkey Fever')

	#pygame.mouse.set_visible(0)

#Create The Backgound



#Prepare Game Objects
	clock = pygame.time.Clock()
	
 
#Main Loop
	
	clock.tick(4)
	pygame.key.set_repeat(1,1)
	slash=0
	down=False
	L=""
	ultrabreak=False
	while ultrabreak==False:
		clock.tick(4)
    #Handle Input Events
    	
		gotten =  pygame.event.get()
		#print gotten, type(gotten)
		#print space
		if (gotten == [] ): #doesn't work if & replaced with "and"... no idea why
			slash=slash+1
			if slash==2:
				slash=0
				print "/",
				L+="/"
		else:
			#clock1.tick(4)
			#print clock2.tick(4)
			slash=0
			for event in gotten:
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN and event.key == K_1:
					#print "PING"
					if down==False:
						down=True
						start = time.time()
						#print start
						#print down
				elif event.type == KEYUP and event.key == K_1:
					down=False
					end = time.time()
					if end-start>0.3:
						print "-",
						L+="-"
					else:
						print ".",
						L+="."
				elif event.type == KEYDOWN and event.key == K_RETURN:
					print ""
				elif event.type == KEYDOWN and event.key ==K_ESCAPE:
					ultrabreak=True
					
    #Draw Everything
    
        #pygame.display.flip()
        
#Game Over
	return L

#this calls the 'main' function when this script is executed
if __name__ == '__main__': a= main()
print a
print textToMorse.MorseToText(a)

