#include <stdio.h>

int main() {
	long n = 600851475143;
	for (int d = 2; d < n; d++) {
		while (n % d == 0) {
			n /= d;
		}
	}
	printf("%ld\n", n);
}
