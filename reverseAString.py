import re
aString="This is a string"
stringSplit=re.split('\s',aString)
print(stringSplit)
reversedString=""
for i in range(len(stringSplit)-1,-1,-1):
	aWord=stringSplit[i]
	##print(aWord)
	reversedString=reversedString+" "+aWord

print(aString)
print(reversedString)
	