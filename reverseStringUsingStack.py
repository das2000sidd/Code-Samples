def push(stack,letter): ## adding one item to list
	stack.append(letter)

def createStack(): ## assigning an empty list as a stack
	stack=[]
	return stack
	
def size(stack):
	return len(stack)
	
def isEmpty(stack): ## function returns true if length of stack is 0
	if (size(stack)==0):
		return true

def pop(stack): ## if stack is empty checks out else returns last item
	if(isEmpty(stack)):
		return -1
	else:
		return stack.pop()	
		
def reverseString(string):
	n=size(string)
	stack=createStack()
	for i in range(0,n):
		push(stack,string[i])
	string=""
	for i in range(0,n,1):
		string+=pop(stack)			
	return string	
	
string1="A very sad day"

reversedString=reverseString(string1)

	##listOfLetters=peek(listOfLetters)
	##print(listOfLetters)

print("The reversed string is:")
print(reversedString)