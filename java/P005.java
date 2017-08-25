public class P005 {
	private static long gcd(long a, long b) {
		if(b == 0) return a;
		return gcd(b, a % b);
	}

	private static long lcm(long a, long b) {
		return a * b / gcd(a, b);
	}

	public static void main(String[] args) {
		long num = 1;
		for(int i = 1; i < 20; i++) {
			num = lcm(num, i);
		}
		System.out.println(num);
	}
}
