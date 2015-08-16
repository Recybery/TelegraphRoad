
import string
#test=string.lower(raw_input('-->'))
D= {}
#'''
import non_ASCII # 
non_ASCII.addStuff(D)
#'''
D["a"]=".-"
D["b"]="-..."
D["c"]="-.-."
D["d"]="-.."
D["e"]="."
D["f"]="..-."
D["g"]="--."
D["h"]="...."
D["i"]=".."
D["j"]=".---"
D["k"]="-.-"
D["l"]=".-.."
D["m"]="--"
D["n"]="-."
D["o"]="---"
D["p"]=".--."
D["q"]="--.-"
D["r"]=".-."
D["s"]="..."
D["t"]="-"
D["u"]="..-"
D["v"]="...-"
D["w"]=".--"
D["x"]="-..-"
D["y"]="-.--"
D["z"]="--.."
D[" "]=""
D['1']=".----"
D['2']="..---"
D['3']="...--"
D['4']="....-"
D['5']="....."
D['6']="-...."
D['7']="--..."
D['8']="---.."
D['9']="----."
D['0']="-----"
D['.']=".-.-.-"
D[',']="--..--"
D['?']="..--.."
D['/']="-..-."
D['@']=".--.-."
D[':']="---..."
D['-']="-....-"
D['\'' ]=".----."#apostrophe
D['/']="-..-."
D['$']="...-..-"
D['"']=".-..-."
D[';']="-.-.-."
D['=']="-...-"
D[chr(127)]="........"#error or erase could be used to erase character in output string with WithDelete function
'''
old morse code just here for thouroughness/ maybe we'll implement someday
#D["seperation sign"]=".-..-"
D["brackets"]="-.--.-"
D["underline"}=..--.-"
D["starting signal"]="-.-.-"
D["end of Message"]=".-.-."
D[closing down]="...-.-"
D[interval (wait)]=".-..."
'''
#D['']

def TextToMorse(a):
	a=string.lower(a)
	B=""
	for i in  range(0,len(a)):
		B+=D[a[i]]+"/"
		
	return B

def getKey(a):
	for i in D.keys():
		if D[i]==str(a):
			return i
	return -1
			
def MorseToText(a):
	B=""
	try:
		F=a.split("/")

	except AttributeError:
		pass
	
	for i in F:
		c= getKey(i)
		if c!=-1:
				B+=c
	return B
#'''
def withDelChar(string): # deletes previous character if character is delete character
	out=""
	for i in range(0,len(string)):
		if(string[i]==chr(127) ):
			out	=out[:-1]
		else:
			out+=string[i ]
	return out
#'''

'''
# use to test above funcions if need
S="hate\x7f 12345678990 /?=.,$ \"fox\" '\' GG brown dog lazy quick over jumped the the"
T=withDelChar(S)
U=TextToMorse(S)
V=MorseToText(U)
print T
print U
print V 
#'''