#include <iostream>
using namespace std;

int main() {
	long n = 600851475143;

	long largest_factor = 0;
	for(long i = 2; i <= n; i++) {
		while(n % i == 0) {
			largest_factor = i;
			n /= i;
		}
	}
	cout << largest_factor << endl;
}
