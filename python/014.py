def chain(n):
	if n < 1000000 and C[n] > 0:
		return C[n]

	if n % 2 == 0:
		length = 1 + chain(n / 2)
	else:
		length = 1 + chain(3 * n + 1)

	# memoize
	if n < 1000000:
		C[n] = length

	return length

C = [0] * 1000000
C[1] = 1

starting_number, longest = 0, 0
for i in range(1, 1000000):
	length = chain(i)
	if length > longest:
		starting_number = i
		longest = length

print(starting_number)
