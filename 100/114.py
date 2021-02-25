def main():
    def f(n):
        if n in memo:
            return memo[n]
        else:
            return 2*f(n-1) - f(n-2) + f(n-4)

    memo = {0:1,1:1,2:1,3:2}
    for i in range(31):
        memo[i] = f(i)

    print(memo[30])

def main2():
    @memo
    def nblocks(n):
        if 0 <= n <= 2:
            return 1
        else:
            return (nblocks(n - 1)  ## 1 black square first
                    + sum(nblocks(n - r - 1) for r in range(3, n))
                    ## red, then 1 black
                    + 1)  ## red block of len n

    assert nblocks(7) == 17
    print(nblocks(50))

main()