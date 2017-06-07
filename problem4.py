# Problem 4 - Largest palindrome product
"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product
of two 3-digit numbers.
"""

n1 = 900
n2 = 900
prevp = 0
prod = 0
sprod = ""
subar1 = []
subar2 = []

while n1 < 1000:
	
	while n2 < 1000:
		prod = n1*n2
		sprod = str(prod)

		for c in sprod:
			subar1.append(c)

		for l in reversed(sprod):
			subar2.append(l)

		if subar1 == subar2 and prod > prevp:
			prevp = prod
			print(prod)

		subar1 = []
		subar2 = []

		n2+=1
	n2=1
	
	n1+=1

