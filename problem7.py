# Problem 7 - 10001st prime
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
2 3 5 7 11 13 17 19 23 29 31 37 41
1 2 3 4 5  6  7  8  9  10 11 12 13
"""
import timeit

start = timeit.default_timer()
##############################

primeCtr = 0
num = 0

while primeCtr < 10000:
	num += 1
	for x in range(2, num): # divisibility check

		if num%x == 0: break
		if x == num-1: 
			# print(num)
			primeCtr+=1

primeCtr+=1 # we need this because 2%2 gives 0 and fails the test, so our primes are detected by the test from 3 and higher
print("\n")
print("Found first " + str(primeCtr) + " prime numbers, and the last is:")
print(num)

##############################
print(timeit.default_timer() - start)
