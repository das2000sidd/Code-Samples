string="Greetings"
		
def getTowerOfHanoi(aString):
	l=len(aString)
	for i in range(l,-1,-1):
		if(i!=0):
			print(aString[0:i])
		elif(i==0):
			for i in range(1,l+1):
				if(i!=1):
					print(aString[0:i])
		
(getTowerOfHanoi(string))