## This is a coding challenge question where given a list numbers we have to return the number of pairs that are in a specified distance


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
	
	
	
def findANumberDistTwo(listOfNumsSorted,numAtDistTwo):
		
		low=0
		high=len(listOfNumsSorted)-1
		while(low <= high):	
			mid=int((low+high)/2)
			if(listOfNumsSorted[mid]==numAtDistTwo):
				return mid
			elif(listOfNumsSorted[mid]> numAtDistTwo):
				high=mid-1
			else:
				if(listOfNumsSorted[mid] < numAtDistTwo):
					low=mid+1
		return -1
		
		
def findNumOfPairAtDistTwo(listOfNums,distance):
	listOfNumsSorted=mergeSort(listOfNums)
	
	noOfPairsAtDistTwo=0
	for aNum in listOfNumsSorted:
		
		positionOfNumAtDistTwo=findANumberDistTwo(listOfNumsSorted,aNum+distance)
		##print("This is the num " + str(aNum))
		##print("This is the position of num at dist 2 " + str(positionOfNumAtDistTwo))
		if(positionOfNumAtDistTwo!=-1):
			noOfPairsAtDistTwo=noOfPairsAtDistTwo+1
	return noOfPairsAtDistTwo
		


def fixedDistance(a, d):
	listOfNumsSorted=mergeSort(a)
	
	noOfPairsAtDistTwo=0
	for aNum in listOfNumsSorted:
		
		positionOfNumAtDistTwo=findANumberDistTwo(listOfNumsSorted,aNum+d)
		##print("This is the num " + str(aNum))
		##print("This is the position of num at dist 2 " + str(positionOfNumAtDistTwo))
		if(positionOfNumAtDistTwo!=-1):
			noOfPairsAtDistTwo=noOfPairsAtDistTwo+1
	return noOfPairsAtDistTwo
	
	
testArray=[1,5,3,4,2]
print(mergeSort(testArray))
sortedTestArray=mergeSort(testArray)
##print(findANumberDistTwo(sortedTestArray,24))
##print(findANumberDistTwo(sortedTestArray,35))	
print(fixedDistance(testArray,2))