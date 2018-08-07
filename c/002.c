#include <stdio.h>

int main() {
	int a = 1;
	int b = 2;
	
	int sum = 0;
	while (a < 4000000) {
		if (a % 2 == 0) {
			sum += a;
		}
		int c = a + b;
		a = b;
		b = c;
	}
	printf("%d\n", sum);
}
