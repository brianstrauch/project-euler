defmodule Problem001 do
    def solve(0, sum) do
        sum
    end

    def solve(n, sum) do
        if rem(n, 3) == 0 or rem(n, 5) == 0 do
            solve(n - 1, sum + n)
        else
            solve(n - 1, sum)
        end
    end
end

IO.puts(Problem001.solve(999, 0))
