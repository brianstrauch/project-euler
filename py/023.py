def abundant(n):
	sum = 0
	for i in range(1, n):
		if n % i == 0:
			sum += i
	return sum > n

A = []
for i in range(28124):
	A.append(abundant(i))

sum = 0
for n in range(28124):
	non_abundant_sum = True
	for a in range(n):
		b = n - a
		if A[a] and A[b]:
			non_abundant_sum = False
			break
	if non_abundant_sum:
		sum += n
print(sum)
