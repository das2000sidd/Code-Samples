A1=120
A2=33
def decimalToBinary(anyNum):
	binaryNum=""
	while(anyNum!=0):
		rem=anyNum%2
		remStr=str(rem)
		binaryNum=binaryNum+remStr
		anyNum=anyNum//2
	binaryNumReversed=""
	
	for i in range(len(binaryNum)-1,-1,-1):
		binaryNumString=binaryNum[i]
		binaryNumReversed=binaryNumReversed+ binaryNumString
		
	return binaryNumReversed
	
	
print("Testing getting binary format of any decimal num")
print(decimalToBinary(A1))
print(decimalToBinary(A2))


B1=1111000
B2=100001
def binaryToDecimal(binaryNum):
	binaryNumAsStr=str(binaryNum)
	decimalForm=0
	lengthOfBinary=len(binaryNumAsStr)
	for i in range(0,len(binaryNumAsStr)):
		numAtPos=int(binaryNumAsStr[i])
		decimalFormForNumAtPos=numAtPos*(2**(lengthOfBinary-i-1))
		
		decimalForm=decimalForm+decimalFormForNumAtPos
	return decimalForm
	
	
print("Testing getting decimal formay of any binary num")
print(binaryToDecimal(B1))	
print(binaryToDecimal(B2))



def decimalToBinaryWithRecursion(anyNum):
	binaryNum=""
	if(anyNum>0):
		rem=anyNum%2
		remStr=str(rem)
		binaryNum=binaryNum+remStr
		return(str(decimalToBinaryWithRecursion(anyNum//2))+binaryNum)
	else:
		return ("")
		


print(decimalToBinaryWithRecursion(33))
print(decimalToBinaryWithRecursion(32))
print(decimalToBinaryWithRecursion(65))
	
