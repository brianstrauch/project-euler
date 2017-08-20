def factorial(n):
	if n < 2: return 1
	return n * factorial(n - 1)

n = factorial(100)

sum = 0
while n > 0:
	sum += n % 10
	n /= 10
print(sum)
