def factorial(n):
	if n < 2: return 1
	return n * factorial(n - 1)

digits = [i for i in range(10)]
count = 1

permutation = 0
for i in range(1, 11):
	remaining = 10 - i
	p = factorial(remaining)
	
	digit = 0
	while count + p <= 1000000:
		digit += 1
		count += p
	permutation = 10 * permutation + digits.pop(digit)
print(permutation)
