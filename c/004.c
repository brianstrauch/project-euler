#include <stdio.h>

int is_palindrome(int n) {
	int forward = n, backward = 0;
	while (n > 0) {
		int digit = n % 10;
		backward = backward * 10 + digit;
		n /= 10;
	}
	return forward == backward;
}

int main() {
	int largest = 0;
	for (int a = 100; a < 1000; a++) {
		for (int b = 100; b < 1000; b++) {
			int product = a * b;
			if (product > largest && is_palindrome(product)) {
				largest = product;
			}
		}
	}
	printf("%d\n", largest);
}
