p = for x <- 100..1000, y <- x..1000, do: x * y
is_palindrome = &(String.reverse(to_string(&1)) == to_string(&1))
IO.puts Enum.max Enum.filter(p, is_palindrome)
