def main():
    def f(m,n):
        if n < m:
            memo[n] = 1
            return memo[n]
        elif n == m:
            memo[n] = 2
            return memo[n]
        else:
            return 2*memo[n-1] - memo[n-2] + memo[n-m-1]

    memo = {}
    m = 50
    n = 0
    limit = 10**6
    while f(m,n) < limit+1:
        print(f(m,n))
        memo[n] = f(m,n)
        n += 1
    print(n)

main()