#include <iostream>
using namespace std;

long gcd(long a, long b) {
	if(b == 0) return a;
	return gcd(b, a % b);
}

long lcm(long a, long b) {
	return a * b / gcd(a, b);
}

int main() {
	long num = 1;
	for(long i = 1; i <= 20; i++) {
		num = lcm(num, i);
	}
	cout << num << endl;
}
