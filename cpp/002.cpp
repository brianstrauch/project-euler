#include <iostream>
using namespace std;

int main() {
	int a = 1, b = 1;
	
	int sum = 0;
	while (a < 4000000) {
		if(a % 2 == 0) {
			sum += a;
		}
		int c = a + b;
		a = b;
		b = c;
	}
	cout << sum << endl;
}
