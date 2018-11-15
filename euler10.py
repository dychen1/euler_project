#function 1: check if prime
def is_prime(num):
	for a in range (2,int(num**0.5)+1):
		if num%a == 0:
			return False
	return True

sum = 2
top_lim = 2000000

for num in range (3, top_lim ,2):
	if is_prime(num):
		sum += num

print(sum)