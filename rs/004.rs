use std::cmp::max;

fn reverse(mut n: i32) -> i32 {
    let mut r = 0;

    while n > 0 {
        r = 10 * r + (n % 10);
        n /= 10;
    }

    r
}

fn palindrome(n: i32) -> bool {
    n == reverse(n)
}

fn main() {
    let mut n = 0;

    for a in 100..1000 {
        for b in 100..1000 {
            let c = a * b;
            if palindrome(c) {
                n = max(n, c);
            }
        }
    }

    println!("{}", n);
}
