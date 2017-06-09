# Problem 5 - Smallest multiple
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

start from 20, check modulo divisions, if not bingo, take higher multiple of 20 and repeat

"""
import timeit
start = timeit.default_timer()
##############################

num = 20

while (num%2+num%3+num%4+num%5+num%6+num%7+num%8+num%9+num%10+num%11+num%12+num%13+num%14+num%15+num%16+num%17+num%18+num%19 > 0):

	num+=20

print(num)


##############################
print(timeit.default_timer() - start)
