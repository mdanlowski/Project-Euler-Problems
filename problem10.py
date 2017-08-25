# Problem 10 - Summation of primes
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
											+ 11 = 28
											+ 13 = 41
Find the sum of all the primes below two million.
------------
If a modulo division of number n > 2 by consequent natural numbers, from 2 to n-1, returns 0 - then number n is not a prime 
'''
import timeit
start = timeit.default_timer()
##############################
primesum = 0
num = 3

while num < 2000000:
	primesum += num
	for x in range(2, num):
		if num%x == 0: 
			primesum -= num
			break
	num += 1
	print(num)

print(primesum + 2)
##############################
print(timeit.default_timer() - start)
