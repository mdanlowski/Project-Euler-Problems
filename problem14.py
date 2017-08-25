# PROBLEM 14, projecteuler.net
bingo = 0
max_len = 2

for num in range(2, 1000000):
	seq_len = 1
	x = num

	while num > 1:
		seq_len += 1
		if num % 2 == 0: num = num/2
		else: num = 3*num + 1

		if seq_len >= max_len:
			max_len = seq_len
			ret = x 

print(max_len, ret)
