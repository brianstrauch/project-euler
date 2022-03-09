f = &(rem(&1, 3) == 0 or rem(&1, 5) == 0)
x = 1..999 |> Enum.filter(f) |> Enum.sum
IO.puts x
