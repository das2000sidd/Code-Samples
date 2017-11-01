## This is code for matrix multiplication of square and rectangular matrices
A=[[1,2,3],[4,5,6]] ## 2*3
B=[[1,4],[2,5],[3,6]] ## 3*2
C=[[1,2,3,4],[5,6,7,8],[9,10,11,12]] ## 3*4
D=[[1,2],[3,4]] ## 2*2
E=[[5,6],[7,8]] ## 2*2
def getAnyMatrixCol(A,i):
	listToReturn=[]
	for eachList in A:
		numToGet=eachList[i]
		listToReturn.append(numToGet)
	return listToReturn
		

print(getAnyMatrixCol(B,1))		

def multiplyTwoMatricesWithFirstMoreCols(matA,matB):
	
	numRowsProd = len(matA)
	numColsProd = len(matB[0])
	if(len(matA[0])!=len(matB)):
		return("Matrix multiplication is not possible")
	else:
			
		prodMatrix=[[0 for x in range(numRowsProd)] for y in range(numColsProd)]
		for row in range(0,numRowsProd):
			for col in range(0,numColsProd):
				rowOfA=matA[row]
				colOfB=getAnyMatrixCol(matB,col)
				for i in range(0,len(rowOfA)):
					for j in range(0,len(colOfB)):
						if(i==j):
							prodMatrix[row][col]=prodMatrix[row][col]+(rowOfA[i]*colOfB[j])
	return prodMatrix		
				
print(multiplyTwoMatricesWithFirstMoreCols(A,B)) ## Works for this
print(multiplyTwoMatricesWithFirstMoreCols(D,E)) ## Works for this
print(multiplyTwoMatricesWithFirstMoreCols(A,D)) ## gives the correct error message that is it not possible


def multiplyTwoMatricesWithSecondMoreCols(matA,matB):
	numRowsProduct=len(matA)
	numColsProduct=len(matB[0])
	if(len(matA[0])!=len(matB)):
		return("Matrix multiplication is not possible")
	else:
		prodMatrix=[[0 for x in range(numColsProduct)] for y in range(numRowsProduct)]
		for row in range(0,numRowsProduct):
			for col in range(0,numColsProduct):
				rowOfMatA=matA[row]
				colOfMatB=getAnyMatrixCol(matB,col)
				for i in range(0,len(rowOfMatA)):
					for j in range(0,len(colOfMatB)):
						if(i==j):
							prodMatrix[row][col]=prodMatrix[row][col]+(rowOfMatA[i]*colOfMatB[j])
	return prodMatrix
	
	
print(multiplyTwoMatricesWithSecondMoreCols(A,C)) ## Works for this
print(multiplyTwoMatricesWithSecondMoreCols(D,E)) ## Works for this
print(multiplyTwoMatricesWithSecondMoreCols(A,E)) ## gives the correct error message that is it not possible
