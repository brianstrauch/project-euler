(define f (lambda (i n)
  (if (< i n)
    (if (= (remainder n i) 0)
      (f i (/ n i))
      (f (+ i 1) n)
    )
    n
  )
))

(f 2 600851475143)
