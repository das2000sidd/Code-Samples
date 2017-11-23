
## In this probllem given two sorted arrays we have to find their median
sortedArray1=[1,3]
sortedArray2=[2]
def getMedian(sortedArray1,sortedArray2):
	combinedSortedArray=[]
	while(len(sortedArray1) > 0 and len(sortedArray2) > 0):
		if(sortedArray1[0]  > sortedArray2[0]):
			combinedSortedArray.append(sortedArray2[0])
			sortedArray2.pop(0)
		else:
			if(sortedArray1[0] < sortedArray2[0]):
				combinedSortedArray.append(sortedArray1[0])
				sortedArray1.pop(0)
				
	combinedSortedArray=combinedSortedArray+sortedArray1
	combinedSortedArray=combinedSortedArray+sortedArray2
	if (len(combinedSortedArray)%2!=0):
		median=combinedSortedArray[int((len(combinedSortedArray))/2)]
	else:
		if(len(combinedSortedArray)%2==0):
			firstNum=combinedSortedArray[int(len(combinedSortedArray)/2)-1]
			secondNum=combinedSortedArray[int(len(combinedSortedArray)/2)]
			median=(firstNum+secondNum)/2
	return median
	
sortedArray3=[1,2,3,4]
sortedArray4=[5,6,7,8]
print(getMedian(sortedArray1,sortedArray2))
print(getMedian(sortedArray3,sortedArray4))
