def divisor_sum(n):
	sum = 0
	for i in range(1, n):
		if n % i == 0:
			sum += i
	return sum

sum = 0
for a in range(10000):
	b = divisor_sum(a)
	if a != b and a == divisor_sum(b):
		sum += a
print(sum)
