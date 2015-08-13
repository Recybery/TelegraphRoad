

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
	screen = pygame.display.set_mode((468, 100))
	pygame.display.set_caption('morse code!!')
	white=(0,0,0)
	pygame.draw.rect(screen, (0,0,0),(200-100,30-10,200,20),20)
	pygame.display.flip()
	#pygame.mouse.set_visible(0) # this makes the cursor dissapear in the program=dumb
	fontobject = pygame.font.Font(None,18)
	screen.blit(fontobject.render(" lasdkjf", 1, white#(255,255,255)
								),
				((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
	pygame.display.flip()
	pygame.display.update()
	
#Prepare Game Objects
	clock = pygame.time.Clock()
	
	pygame.key.set_repeat(1,1)## makes it so that holding down key creates events
	slash=0 #keeps track of cycles of loop for "/" printing/ concatenating
	down=False #needed in conjuction w/pygeme.key.set_repeat() to keep line 75 from going when key held down
	autoreturn=0 #when reaches a certain number prints "" automatically
	
	dih=0.1 #length seconds of a . i.e di in morse
	dah=3*dih #from internet: dah=3 di's
	
	L="" #creates string of {"/",".""-"} to be translated into text
	ultrabreak=False
	#Main Loop
	while not ultrabreak:
		#delays loop so doesn't go too fast
		clock.tick(1/(2*dih))
    	# like I said in my overly long git commit message, delays 1/speed (di)seconds
    	#Handle Input Events
		gotten =  pygame.event.get()
		#print gotten, type(gotten)
		#print space
		if(autoreturn>=55):# may need to be adjusted per display
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
			#clock1.tick(4)
			#print clock2.tick(4)
			slash=0
			for event in gotten:
				#if event.type==KEYUP:
				
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
					if end-start>dah: #from internet: dash =3 di's
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
				elif event.type == KEYDOWN and event.key ==K_ESCAPE:
					print ""
					ultrabreak=True
				elif event.type== KEYDOWN and event.key==K_SPACE:
					print "/ /",
					
    #Draw Everything
    
        #pygame.display.flip()
        
#Game Over
	
	return L

#this calls the 'main' function when this script is executed
if __name__ == '__main__': a= main()
print textToMorse.MorseToText(a)

