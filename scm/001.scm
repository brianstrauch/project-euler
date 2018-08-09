(define f (lambda (i n sum)
  (if (< i n)
    (if (or (= (remainder i 3) 0) (= (remainder i 5) 0))
      (f (+ i 1) n (+ sum i))
      (f (+ i 1) n sum)
    )
    sum
  )
))

(f 1 1000 0)
