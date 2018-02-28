## check if number is divisible by 3 without modulus function

def check_divisible_by_3(num):
	if(num==3 or num==6 or num==9 or num==0):
			return True
	else:
		string_num=str(num)
		sum_digits=0
		for i in range(0,len(string_num)):
			if(string_num[i]!='-'):
				digit_num = int(string_num[i])
				sum_digits+=digit_num
		if(sum_digits==3 or sum_digits==6 or sum_digits==9):
			return True
		elif(sum_digits>=10):
			return check_divisible_by_3(sum_digits)
		else:
			return False
	
	
print(check_divisible_by_3(279))
print(check_divisible_by_3(298))
print(check_divisible_by_3(25))
print(check_divisible_by_3(27))
print(check_divisible_by_3(3126))
print(check_divisible_by_3(-279))
print(check_divisible_by_3(0))
