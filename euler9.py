def multiply_condition(a,b,c):
	if c**2 == a**2 + b**2:
		return True

def check_pythag(a,b,c):
	if a < b < c and a + b + c == 1000 and multiply_condition(a,b,c):
		return True

for a in range (1,1000):
	for b in range (a,1000):
		for c in range (b, 1000):
			if check_pythag(a,b,c):
				print(a*b*c)

