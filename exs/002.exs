defmodule Problem002 do
    def solve(a, _b, sum) when a > 4_000_000 do
        sum
    end

    def solve(a, b, sum) do
        if rem(a, 2) == 0 do
            solve(b, a + b, sum + a)
        else
            solve(b, a + b, sum)
        end
    end
end

IO.puts Problem002.solve(0, 1, 0)
