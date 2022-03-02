f = fn n -> rem(n, 3) == 0 or rem(n, 5) == 0 end
x = Enum.sum(Enum.filter(1..999, f))
IO.puts(x)
