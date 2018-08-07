#include <iostream>
using namespace std;

int main() {
	long n = 600851475143;
	for(long i = 2; i < n; i++) {
		while(n % i == 0) {
			n /= i;
		}
	}
	cout << n << endl;
}
