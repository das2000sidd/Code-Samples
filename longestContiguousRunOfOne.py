##Given a binary string(a string consisting only of 0s and 1s) find the length of the longest contiguous occurrence of 1s.

A='00001111111110001111'
ASplit=A.split('0')
def getTheNoOfOnesByStartingPos(aListOfNums):
	
		lengthOfOnesList={}
		for anItem in aListOfNums:
			if(anItem!=''):
				indexReturned=aListOfNums.index(anItem)
				lengthOfOnesList[indexReturned]=len(anItem)
		return lengthOfOnesList

dictOfOneCountByStartingPos=(getTheNoOfOnesByStartingPos(ASplit))

def findLongestLength(dictOfContiguousOneLengths):
	highestCountOfOne=0
	for startingPos,noOfOnes in dictOfContiguousOneLengths.items():
		if(noOfOnes >highestCountOfOne):
			highestCountOfOne=noOfOnes
	return highestCountOfOne
	
print(findLongestLength(dictOfOneCountByStartingPos))


## Works but not sure if best solution. Need to implement binary search	