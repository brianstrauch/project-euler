fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn lcm(a: i64, b: i64) -> i64 {
    a * b / gcd(a, b)
}

fn main() {
    let mut n = 1;
    for i in 1..=20 {
        n = lcm(n, i);
    }
    println!("{}", n);
}
