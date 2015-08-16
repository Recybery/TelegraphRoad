keygetter.py takes keystroke input from the keyboard or an arduino and translates it into
text via Morse code. 

use the "1" key or use the arduino switch key to enter your message
press the "2" key to enter in a slash manually. (note one slash is a space between characters, and N slashes in a row will be N-1 spaces in a row)
press F1 to translate immediately in pygame window
press F2 to translate immediately in console
press tab to toggle on and off the automatic creation of slashes (which represent spaces between words and characters) 

you can cheat by pressing q and w to enter . and - respectively or just . and - and / on the keyboard

press escape to exit program and have all of what you inputed by translated in the command line

keygetter should work even if it fails to connect to serial port
__________________________________________________________________________________________________
pyserial_test.py takes text from the command line and sends it to the arduino, which beeps the text out in morse code

both programs I believe should work on linux and windows