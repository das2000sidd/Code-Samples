##Given 2 numbers m and n , find if the sum m+n has the same number of digits as n . If true then print m+n otherwise print n.
m=90
n=230
sum=m+n ## 320
def doDivision(aNumber):
	noOfDigits=1
	while(aNumber!=0):
		if(aNumber//10!=0):
			noOfDigits=noOfDigits+1
		aNumber=aNumber//10	
	return noOfDigits

if(doDivision(n)==doDivision(sum)):
	print(sum)

m1=900
n1=145
sum1=m1+n1
if(doDivision(n1)!=doDivision(sum1)):
	print(n1)