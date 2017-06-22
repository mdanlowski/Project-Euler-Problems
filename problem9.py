# Problem 9 - Special Pythagorean triplet
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import timeit

start = timeit.default_timer()
##############################

a=1
b=2
c=997

while b<c:
	while a < b:
		if a**2 + b**2 == c**2: 
			print("Product in question:", a*b*c, "Test checks:", a+b+c, a, b, c, )
			exit
		a+=1
		c-=1
	a=1
	b+=1
	c=1000-b-a		

##############################
print("Time:", timeit.default_timer() - start)