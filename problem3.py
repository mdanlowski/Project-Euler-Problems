# Problem 3 - Largest prime factor
"""
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?

"""

num = 600851475143 # FAULT FOR EVEN INPUTS!!!!!
div = 2

check = 1
target = 0
found = False
factors = []

while div < num:
	if num % div == 0: factors.append(div)

	for x in range(0, len(factors)): # REMEMBER: IN range(), SECOND TERM IS IMPLICITLY AN OPEN BOUND, SO NO -1 NEEDED
		check *= factors[x]

		if check == num:
			target = factors[x]		 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			found = True			 # break the while loop

	if found: break

	check = 1

	div += 1

print(target)
print(factors)
