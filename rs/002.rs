fn even(n: i32) -> bool {
    n % 2 == 0
}

fn main() {
    let mut a = 1;
    let mut b = 1;
    let mut sum = 0;

    while a <= 4_000_000 {
        if even(a) {
            sum += a;
        }

        let c = a + b;
        a = b;
        b = c;
    }

    println!("{}", sum);
}
