#include <iostream>
using namespace std;

bool palindrome(int n) {
	int forwards = n, backwards = 0;
	while(n > 0) {
		backwards = 10 * backwards + n % 10;
		n /= 10;
	}
	return forwards == backwards;
}

int main() {
	int largest = 0;
	for(int a = 100; a < 1000; a++) {
		for(int b = a + 1; b < 1000; b++) {
			int product = a * b;
			if(product > largest && palindrome(product)) {
				largest = product;
			}
		}
	}
	cout << largest << endl;
}
