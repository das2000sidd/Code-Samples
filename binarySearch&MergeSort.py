A=[1,4,2,6,18,36,9,17]

def mergeSort(listOfNum):
	if len(listOfNum) < 2:
		return listOfNum
	result=[]
	mid=int(len(listOfNum)/2)
	y=mergeSort(listOfNum[:mid])
	z=mergeSort(listOfNum[mid:])
	
	while(len(y) > 0) and (len(z) > 0):
		if(y[0] > z[0]):
			result.append(z[0])	
			z.pop(0)
		else:
			result.append(y[0])
			y.pop(0)
	result=result+y
	result=result+z
	return result

## iterative method of sorting
def binarySearch(arrayToSearch,arraySize,numToFind):
	start=0
	end=arraySize-1
	while(start <= end):
		mid=(start+end)/2
		mid=int(mid)
		if(arrayToSearch[mid]==numToFind):
			return mid
		elif(numToFind < arrayToSearch[mid]):
			end=mid-1
		else:
			if(numToFind > arrayToSearch[mid]):
				start=mid+1
	return -1

## recursive method of sorting
def binarySearchWithRecursion(arrayToSearch,arrayStartIndex,arrayStopIndex,numToFind):
	
	if(arrayStartIndex > arrayStopIndex):
		return -1
	else:
		mid=arrayStartIndex+(arrayStopIndex-arrayStartIndex)/2
		mid=int(mid)
		if(numToFind==arrayToSearch[mid]):
			return mid
		elif(numToFind < arrayToSearch[mid]):
			return binarySearchWithRecursion(arrayToSearch,arrayStartIndex,mid-1,numToFind)
		else:
			if(numToFind > arrayToSearch[mid]):
				return binarySearchWithRecursion(arrayToSearch,mid+1,arrayStopIndex,numToFind)


sizeOfA=len(A)	
sortedA=mergeSort(A)
print(sortedA)
posOfSix = binarySearch(sortedA,len(sortedA),6)	
print(posOfSix)

testingRecursion =binarySearchWithRecursion(sortedA,0,len(sortedA)-1,6)
print(testingRecursion)