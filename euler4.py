#function 1: products of two 3-digit numbers
#function 2: verify if palindrome

def product(largest_palin):
	for outer_num in range(100, 1000):
		for inner_num in range(100, 1000):
			prod = outer_num * inner_num
			
			if palin(prod) and prod >= largest_palin: 
				largest_palin = prod
				
	return largest_palin
	
def palin(num):
	if str(num) == str(num)[::-1]:
		return True
		
largest_palin = 0

print(product(largest_palin))