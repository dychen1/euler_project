#sum of square of first 100 nat numbers
sum1 = 0

for x in range(1,101):
	sum1 += x**2

#square of the sum of first 100 nat numbers
sum2 = 0

for y in range(1,101):
	sum2 += y

sum2 = sum2**2

ans = abs(sum1 - sum2)

print(ans)