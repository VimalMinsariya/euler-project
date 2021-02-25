def main():
    charateristicf = {1: [1, -1]}
    a = [1,1]
    n = 2
    while a[-1] % 10**6 != 0:
        f = charateristicf[n-1]
        x1 = f + [0] * n
        x2 = [0] * n + f
        result = []
        for j in range(len(x1)):
            result.append(x1[j] - x2[j])
        charateristicf[n] = result
        t = 0
        for j in range(1, n + 1):
            t -= charateristicf[n][j] * a[n - j]
        a.append(t)
        print(t)
        n += 1
    print(n-1)

main()