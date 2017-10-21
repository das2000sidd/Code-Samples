def push(stack,letter):
	stack.append(letter)
	
def createStack():
	stack=[]
	return stack
	

def size(stack):
	return len(stack)
	
def isEmpty(stack):
	if(size(stack)==0):
		return true
		
def peek(stack):
	return stack[len(stack)-1]

		
def pop(stack):
	if(isEmpty(stack)==True):
		return -1
	else:
		return stack.pop()

		
def generateTopOfKShapedWord(aString):
	lengthString=size(aString)
	stack=createStack()
	for i in range(0,lengthString):
		push(stack,aString[i])
	##print(stack)	
	for i in range(lengthString,0,-1):
		stringReturned=peek(stack)
		
		## last occurence of item in list is indexOfStringReturned
		indexOfStringReturned=len(stack) - stack[::-1].index(stringReturned) - 1
		
		stringtoPrint=''.join(stack[0:indexOfStringReturned+1])
		print(stringtoPrint)
		##stack.pop()
		pop(stack)
				
					
def generateBottomOfKShapedWord(aString):
	lengthString=size(aString)
	stack=createStack()
	for i in range(0,lengthString):
		push(stack,aString[i])
	
	listOfStrings=[] ## generate all possible lengths of word and store in this
	for i in range(0,len(stack),1):
		lastItemOfStack=peek(stack)
		indexOfLastItem=len(stack) - stack[::-1].index(lastItemOfStack) - 1
		stringtoPrint=''.join(stack[0:indexOfLastItem+1])
		listOfStrings.append(stringtoPrint)
		
		##stack.pop()
		pop(stack)
	
	for i in range(len(listOfStrings)-1,-1,-1):
		if(len(listOfStrings[i])!=1): ## first letter of word already printed by generateTopOfTowerOfHanoi(aString) function, so not needed again
			print(listOfStrings[i])	
			
			
def generateKShapedWord(aString):
	generateTopOfKShapedWord(aString)
	generateBottomOfKShapedWord(aString)
			
									
		
generateKShapedWord("Exaggerated") 
print("\n")
generateKShapedWord("Tragic")
## This only works for one word. Not a sentence		
		
## Expected Output

##Exaggerated
##Exaggerate
##Exaggerat
##Exaggera
##Exagger
##Exagge
##Exagg
##Exag
##Exa
##Ex
##E
##Ex
##Exa
##Exag
##Exagg
##Exagge
##Exagger
##Exaggera
##Exaggerat
##Exaggerate
##Exaggerated


##Tragic
##Tragi
##Trag
##Tra
##Tr
##T
##Tr
##Tra
##Trag
##Tragi
#Tragic
			