from math import sqrt

n = 600851475143
largest_factor = 0
for i in range(2, int(sqrt(n)) + 1):
	while n % i == 0:
		n /= i
		largest_factor = i
print(largest_factor)
