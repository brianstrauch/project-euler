#include <stdio.h>

long gcd(long a, long b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

long lcm(long a, long b) {
	return a * b / gcd(a, b);
}

int main() {
	long n = 1;
	for (int i = 1; i <= 20; i++) {
		n = lcm(n, i);
	}
	printf("%ld\n", n);
}
