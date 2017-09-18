A=[3,14,19,36,75,90,130,140,160,182,189,196]

def findIndexOfHighestNumberLessThanANo(aList,aNum):
	theIndexToSearchFor=0
	for index in range(0,len(aList),1):
		if(aList[index] > aNum):
			return index-1
			break
		else:
			if(aNum > aList[index] and index==len(aList)-1):
				return (len(aList)-1)

print(len(A))
print(findIndexOfHighestNumberLessThanANo(A,64)) ## working gives 3
print(findIndexOfHighestNumberLessThanANo(A,96)) ## working gives 5
print(findIndexOfHighestNumberLessThanANo(A,144)) ## working gives 7
print(findIndexOfHighestNumberLessThanANo(A,159)) ## working gives 7
print(findIndexOfHighestNumberLessThanANo(A,139)) ## working gives 6

print(findIndexOfHighestNumberLessThanANo(A,197)) ## working gives 11


