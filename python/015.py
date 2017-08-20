def factorial(n):
	if n < 2: return 1
	return n * factorial(n - 1)

paths = factorial(40) / (factorial(20) * factorial(20))
print(paths)
