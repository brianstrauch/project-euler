fib = Stream.unfold({0, 1}, fn {a, b} -> {a, {b, a + b}} end)
even? = &(rem(&1, 2) == 0)
IO.puts fib |> Enum.take_while(&(&1 < 4_000_000)) |> Enum.filter(even?) |> Enum.sum
