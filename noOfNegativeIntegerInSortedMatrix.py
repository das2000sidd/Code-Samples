## This is an interview question where in a row wise and col wise sorted matrix we find number of negative integers


A=[[-3,-2,-1,1],[-2,2,3,4],[4,5,7,8]]
B=[[-7,-3,-2],[-3,-2,5],[-1,1,7]]

def findOccurenceOfFirstNegativeInteger(aSortedListOfNumberLists):
	dictToStoreFirstOccurence={}
	for i in range(0,len(aSortedListOfNumberLists)):
		result=-1
		low=0
		high=len(aSortedListOfNumberLists[i])-1
		while(low <= high):
			mid=low+(high-low)/2
			mid=int(mid)
			if(aSortedListOfNumberLists[i][mid] < 0):
				result=mid
				high=mid-1
					
			
			else:
					if(aSortedListOfNumberLists[i][mid] > 0):
						high=mid-1
					else:
						low=mid+1
		dictToStoreFirstOccurence[i]=result
	return dictToStoreFirstOccurence
		
print("This is the position of the smallest negative no in each of the lists for list A")		
print(findOccurenceOfFirstNegativeInteger(A))
print("This is the position of the smallest negative no in each of the lists for list B")		
print(findOccurenceOfFirstNegativeInteger(B))


def findOccurenceOfLastNegativeInteger(aSortedListOfNumberLists):
	dictToStoreLastOccurence={}
	for i in range(0,len(aSortedListOfNumberLists)):
		result=-1
		low=0
		high=len(aSortedListOfNumberLists[i])-1
		while(low <= high):
			mid=low+(high-low)/2
			mid=int(mid)
			if(aSortedListOfNumberLists[i][mid] < 0):
				result=mid
				low=mid+1
					
			
			else:
					if(aSortedListOfNumberLists[i][mid] > 0):
						high=mid-1
					else:
						low=mid+1
		dictToStoreLastOccurence[i]=result
	return dictToStoreLastOccurence


print("This is the position of the largest negative no in each of the lists of list A")	
print(findOccurenceOfLastNegativeInteger(A))
print("This is the position of the largest negative no in each of the lists of list B")	
print(findOccurenceOfLastNegativeInteger(B))


def getDictOfNegativeIntegersInSortedMatrix(aSortedListOfNumberLists):
	firstOccurencesOfNegativeNumInListDict=findOccurenceOfFirstNegativeInteger(aSortedListOfNumberLists)
	lastOccurencesOfNegativeNumInListDict=findOccurenceOfLastNegativeInteger(aSortedListOfNumberLists)
	noOfNegativeIntegers={}
	for key,value in firstOccurencesOfNegativeNumInListDict.items():
		noOfNegativeIntPerList=0
		for key1,value1 in lastOccurencesOfNegativeNumInListDict.items():
			if(key==key1):	
				if(value!=-1 and value1!=-1):
					noOfNegativeIntPerList=value1-value+1
					noOfNegativeIntegers[key]=noOfNegativeIntPerList
					
	return 	noOfNegativeIntegers
	
def totalNoOfNegativeInteger(aSortedListOfNumberLists):
	dictOfNegtiveInts=	getDictOfNegativeIntegersInSortedMatrix(aSortedListOfNumberLists)
	totalNegativeInts=0
	for key,value in dictOfNegtiveInts.items():
		totalNegativeInts=totalNegativeInts+value
	return 	totalNegativeInts



print("This is the dictionary of no of negative numbers per list for A")	
print(getDictOfNegativeIntegersInSortedMatrix(A))	
print("This is the total no of negative numbers in the list for list A")
print(totalNoOfNegativeInteger(A))	
print("This is the dictionary of no of negative numbers per list for B")	
print(getDictOfNegativeIntegersInSortedMatrix(B))	
print("This is the total no of negative numbers in the list for list B")
print(totalNoOfNegativeInteger(B))	
	