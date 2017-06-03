# Problem 1 - Multiples of 3 and 5
"""
 If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.
 Find the sum of all the multiples of 3 or 5 below 1000.

Let 3k be a integer multiple of 3 and 5k be a integer multiple of 5.
If then x = [1:1000], 

"""

sumSet = []
total = 0

for x in range(1, 1000):
	if x%3 == 0:
		#print(x)
		sumSet.append(x)

	if x%5 == 0 and x%3 != 0:
		#print(x)
		sumSet.append(x)

print(sumSet)

for num in sumSet:
	total += num

print(total)