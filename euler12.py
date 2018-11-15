triangle = 0
count = 0
factor_count = 0
limit = 500

while True:
    triangle += count
    count += 1
    factor_count = 0
    for n in range(1, triangle):
    	if triangle%n == 0:
    		factor_count += 1
    	print(factor_count)
    if factor_count >= limit:
    	print(triangle)
    	break
 #TAKES WAY TOO LONG

 ############################ efficient solution
#import math
#from time import time
#t = time()
#def divisors(n):
#    number_of_factors = 0
#    for i in range(1, int(math.ceil(math.sqrt(n)))):
#        if n % i == 0:
#            number_of_factors +=2
#        else:
#            continue
#    return number_of_factors

#x=1
#for y in range(2,1000000):
#    x += y
#    if divisors(x) >= 500:
#        print (x)
#
#tt = time()-t
#print (tt)

###