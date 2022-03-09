f = &(rem(&1, 3) == 0 or rem(&1, 5) == 0)
IO.puts 1..999 |> Enum.filter(f) |> Enum.sum
