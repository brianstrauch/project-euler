f = &(rem(&1, 3) == 0 or rem(&1, 5) == 0)
x = Enum.sum Enum.filter(1..999, f)
IO.puts x
