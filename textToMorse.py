import string
#test=string.lower(raw_input('-->'))

D= {}
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
D['1']="....-"
D['2']="...--"
D['3']="..---"
D['4']=".----"
D['5']="-----"
D['6']="----."
D['7']="---.."
D['8']="--..."
D['9']="-...."
D['0']="....."
def TextToMorse(a):
	B=""
	for i in a:
		B+=D[i]+"/"
	return B

def getKey(a):
	for i in D.keys():
		if D[i]==str(a):
			return i
	return -1
			
def MorseToText(a):
	B=""
	F=a.split("/")
	for i in F:
		c= getKey(i)
		if c!=-1:
				B+=c
	return B
#print MorseToText(TextToMorse("ni hao shi jie 1234567890 the lazy fox jumped over the brown dog"))
'''
for i in test:
		B+=D[i]+"/"
print B
#'''

