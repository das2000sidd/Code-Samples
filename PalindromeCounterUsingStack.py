## This is a coding challenge where we have to find the number of palindromic strings within a string

import time

start_time=time.time()
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
	
	
def countPalindromes(aString):
	listofAllPalindromes=[]
	palindromicWords=0
	
	for position in range(0,len(aString)+1):
		for size in range(position+1,len(aString)+1):
			anyString=aString[position:size]
			anyStringReversed=reverseString(anyString)
			if(anyStringReversed==anyString):
				palindromicWords+=1
				
	return palindromicWords
	
	
aString="abccba"	
print(countPalindromes(aString))

print("--- %s seconds ---" % (time.time() - start_time))
