def insertionSort2(A,lengthA):
	valToInsert=0
	lengthA=len(A)
	for i in range(1,lengthA,1):
		valToInsert=A[i]
		holePos=i
		while(holePos > 0 and A[holePos-1] > valToInsert):
			A[holePos]=A[holePos-1]
			holePos=holePos-1
			A[holePos]=valToInsert
	return A	
		
		
A=[1,4,2,6,18,36,9,17]
	
		
sortedList1=insertionSort2(A,len(A))
print("Trying insertion sort again")
print(sortedList1)