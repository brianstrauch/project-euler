#include <stdbool.h>
#include <stdio.h>

#define MAX 1000000

int main() {
	bool prime[MAX];
	for (int i = 0; i < MAX; i++) {
		prime[i] = true;
	}
	prime[0] = prime[1] = false;

	for (int i = 2; i < MAX; i++) {
		if (prime[i]) {
			for (int j = 2 * i; j < MAX; j += i) {
				prime[j] = false;
			}
		}
	}

	int count = 0;
	for (int i = 0; i < MAX; i++) {
		if (prime[i]) {
			count++;
			if (count == 10001) {
				printf("%d\n", i);
				break;
			}
		}
	}
}
