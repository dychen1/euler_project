#function 1: check if divisible by numbers between 1 to 20
def divisible(num):
	for denum in range (2,21):
		if num%denum != 0:
			return False
	return True

#increment numbers until divisible by all numbers between 1 to 20 
num = 20
while True:
	if divisible(num) == True:
		break
	num += 20

print (num)