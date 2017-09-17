## This code for the file testingChrIndexFinding.txt uses binary search to find the first and last index of 
## an item in a sorted list. The motivation behind this code was this is useful to find first and last item in a list for subsequent slicing
import re
def readTestFile(file): ## Working fine
	handle=open(file)
	lines="\n"
	for line in handle:
		lines+=line
	handle.close()
	return lines
	
chrLociread = readTestFile("testingChrIndexFinding.txt") ## a multi sample vcf

def extractLinesWithVariants(chrLociread): ## Working fine
	linesRead = re.split("\n",chrLociread)
	linesRead.pop(0)
	linesRead.pop(len(linesRead)-1)
	return linesRead
	
linesToAList=extractLinesWithVariants(chrLociread)
listAsInt=[int(x) for x in linesToAList]
print(listAsInt)

def findFirstOccurenceOfAnyChr(listOfChr,lenListOfChr,toFindIndexOf):
	low=0
	high=lenListOfChr-1
	result=-1
	while(low <= high):
		mid=low+(high-low)/2
		mid=int(mid)
		if(toFindIndexOf==listOfChr[mid]):
			result=mid
			high=mid-1
		else:
			if(toFindIndexOf < listOfChr[mid]):
				high=mid-1
			else:
				low=mid+1
	return result
	
x=findFirstOccurenceOfAnyChr(listAsInt,len(linesToAList),10)
print(x)

def findLastOccurenceOfAnyChr(listOfChr,lenListOfChr,toFindIndexOf):
	low=0
	high=lenListOfChr-1
	result=-1
	while(low <= high):
		mid=low+(high-low)/2
		mid=int(mid)
		if(toFindIndexOf==listOfChr[mid]):
			result=mid
			low=mid+1
		else:
			if(toFindIndexOf < listOfChr[mid]):
				high=mid-1
			else:
				low=mid+1
	return result
	
y=findLastOccurenceOfAnyChr(listAsInt,len(linesToAList),2)
print(y)
