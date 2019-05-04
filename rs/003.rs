fn main() {
    let mut n: i64 = 600_851_475_143;
    let mut i = 2;

    while i < n {
        while n % i == 0 {
            n /= i;
        }
        i += 1;
    }

    println!("{}", n);
}
