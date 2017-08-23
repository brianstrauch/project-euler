public class P003 {
	public static void main(String[] args) {
		long n = 600851475143L;
		long largestFactor = 0;
		for(int i = 2; i <= n; i++) {
			while(n % i == 0) {
				n /= i;
				largestFactor = i;
			}
		}
		System.out.println(largestFactor);
	}
}
