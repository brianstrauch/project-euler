class Problem004 {
	private static boolean palindrome(int n) {
		int forward = n, reverse = 0;
		while (n > 0) {
			reverse = 10 * reverse + n % 10;
			n /= 10;
		}
		return forward == reverse;
	}

	public static void main(String[] args) {
		int largestPalindrome = 0;
		for (int a = 100; a < 1000; a++) {
			for (int b = a; b < 1000; b++) {
				int product = a * b;
				if (product > largestPalindrome && palindrome(product)) {
					largestPalindrome = product;
				}
			}
		}
		System.out.println(largestPalindrome);
	}
}
