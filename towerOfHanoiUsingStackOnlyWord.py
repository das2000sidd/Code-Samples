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
		
		
def generateTopOfTowerOfHanoi(aString):
	lengthString=size(aString)
	stack=createStack()
	for i in range(0,lengthString):
		push(stack,aString[i])
		
	for i in range(lengthString,0,-1):
		stringReturned=peek(stack)
		
		indexOfStringReturned=stack.index(stringReturned)
		
		stringtoPrint=''.join(stack[0:indexOfStringReturned+1])
		print(stringtoPrint)
		stack.pop()
				
					
def generateBottomOfTowerOfHanoi(aString):
	lengthString=size(aString)
	stack=createStack()
	for i in range(0,lengthString):
		push(stack,aString[i])
	
	listOfStrings=[] ## generate all possible lengths of word and store in this
	for i in range(0,len(stack),1):
		lastItemOfStack=peek(stack)
		indexOfLastItem=stack.index(lastItemOfStack)
		stringtoPrint=''.join(stack[0:indexOfLastItem+1])
		listOfStrings.append(stringtoPrint)
		
		stack.pop()
	
	for i in range(len(listOfStrings)-1,-1,-1):
		if(len(listOfStrings[i])!=1): ## first letter of word already printed by generateTopOfTowerOfHanoi(aString) function
			print(listOfStrings[i])	
			
			
def generateTowerOfHanoi(aString):
	generateTopOfTowerOfHanoi(aString)
	generateBottomOfTowerOfHanoi(aString)
			
									
		
generateTowerOfHanoi("Greetings") 

## This only works for one word. Not a sentence		
		

			