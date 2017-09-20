## This is python code for a version of binary search where given a sorted list, we can retrieve index
## of highest number less than a particular number from the list as well as index of smallest number
##greater than unknown number. An application of this logic would be given a large sorted file of human genetic
## variants by chromosome number and position on the chromosome, it can be used to pull out variants in specific genes
## with known start and end positions on a chromosome instead of using linear search.

A=[3,14,19,36,75,90,130,140,160,182,189,196]


def findIndexOfHighestNumberOnListLessThanUnknown(arrayToSearch,arraySize,numToFind): ## for chrom end
	start=0
	end=arraySize-1
	while(start <= end):
		mid=(start+end)/2
		mid=int(mid)
		if(numToFind > arrayToSearch[mid] and numToFind < arrayToSearch[mid+1]):
			return mid
		elif(numToFind > arrayToSearch[mid]):
				start=mid+1
		else:
			if(numToFind < arrayToSearch[mid]):
				end=mid-1
	return -1

print("Testing if find index of highest number on list less than an unknown number is working or not")
print(findIndexOfHighestNumberOnListLessThanUnknown(A,len(A),64)) ##   3
print(findIndexOfHighestNumberOnListLessThanUnknown(A,len(A),96)) ##   5
print(findIndexOfHighestNumberOnListLessThanUnknown(A,len(A),144)) ##   7
print(findIndexOfHighestNumberOnListLessThanUnknown(A,len(A),159)) ##   7
print(findIndexOfHighestNumberOnListLessThanUnknown(A,len(A),139)) ##   6


def tryingtheFindIndexOfSmallestNumberOnListGreaterThanUnknownNo(arrayToSearch,arraySize,numToFind):
	start=0
	end=arraySize-1
	while(start <= end):
		mid=(start+end)/2
		mid=int(mid)
		if(numToFind < arrayToSearch[mid] and numToFind > arrayToSearch[mid-1]):
			return mid
		elif(numToFind > arrayToSearch[mid]):
				start=mid+1
		else:
			if(numToFind < arrayToSearch[mid]):
				end=mid-1
	return -1	
			
	
	
print("Testing if return of index of smallest number on list greater than an user supplied no is working or not")
print(tryingtheFindIndexOfSmallestNumberOnListGreaterThanUnknownNo(A,len(A),108)) ## 6
print(tryingtheFindIndexOfSmallestNumberOnListGreaterThanUnknownNo(A,len(A),188)) ## 10
print(tryingtheFindIndexOfSmallestNumberOnListGreaterThanUnknownNo(A,len(A),193)) ## 11
print(tryingtheFindIndexOfSmallestNumberOnListGreaterThanUnknownNo(A,len(A),197)) ## -1


