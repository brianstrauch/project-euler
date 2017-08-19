def palindrome(n):
	forward = n
	reverse = 0
	while n > 0:
		digit = n % 10
		n /= 10
		reverse = reverse * 10 + digit
	return forward == reverse

largest = 0
for a in range(100, 1000):
	for b in range(100, 1000):
		product = a * b
		if product > largest and palindrome(product):
			largest = product
print(largest)
