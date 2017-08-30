(define f (lambda (a b sum)
  (if (< a 4000000)
    (if (= (remainder a 2) 0)
      (f b (+ a b) (+ sum a))
      (f b (+ a b) sum)
    )
    sum
  )
))

(f 1 2 0)
