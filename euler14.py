def collatz_seq(n):
	count = 1
	while n != 1:
		if n%2 == 0:
			n = n//2
		else:
			n = 3*n+1
		count += 1
	return count

culum_count = 0
top = 1000000
bot = top//2
for start in range (top, bot, -1):
	collatz_count = collatz_seq(start)

	if collatz_count >= culum_count:
		largest_collatz = start
		culum_count = collatz_count

print(largest_collatz)
print(culum_count)