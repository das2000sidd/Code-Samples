A=[[1,2,3],[4,5,6],[7,8,9]]

def getTranspose(A):
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
		
 

transposeOfA=getTranspose(A)
print(A)
print(transposeOfA)