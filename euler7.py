prime = [2]
num = 3


while len(prime) <= 10000:
	factor = []
	for denum in range(3, num, 2):
		if num%denum == 0:
			factor.append(num)
	
	if len(factor) == 0:
		prime.append(num)
		
	num += 2

print (prime[10000])
