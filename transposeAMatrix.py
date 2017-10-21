A=[[1,2,3],[4,5,6],[7,8,9]]

def getTransposeNotInPlace(A):
	B=[[0 for x in range(len(A[0]))] for y in range(len(A))]
	
	for i in range(0,len(A)):
		length=len(A[i])
		for j in range(0,length):
			if(i!=j):
				B[i][j]=A[j][i]
			else:
				if(i==j):
					B[i][j]=A[i][j]
				
	return B		
		
 

transposeOfA=getTransposeNotInPlace(A)
print("This is the original matrix")
print(A)
print("This is transposing using new matrix")
print(transposeOfA)

def getTransposeInPlace(A):
	
	
	for i in range(0,len(A)):
		length=len(A[i])
		for j in range(0,length):
			if(i>j):
				k=A[i][j]
				A[i][j]=A[j][i]
				A[j][i]=k
			
				
	return A

print("This is transpose in place")	
print(getTransposeInPlace(A))
