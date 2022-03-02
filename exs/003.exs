defmodule Problem003 do
    def solve(n, d) when n == d do
        n
    end

    def solve(n, d) do
        if rem(n, d) == 0 do
            solve(div(n, d), d)
        else
            solve(n, d + 1)
        end
    end
end

IO.puts(Problem003.solve(600_851_475_143, 2))
