def n_reverse(n):
    result = 0
    while n > 0:
        n, r = divmod(n,10)
        result = 10*result + r
    return result

def ispalindromic(n):
    r = n_reverse(n)
    if n == r:
        result = True
    else:
        result = False
    return result

def isLychrel(n):
    cnt = 1
    result = True
    while cnt < 50:
        n = n + n_reverse(n)
        if ispalindromic(n):
            result = False
            break
        cnt += 1
    return result

def main():
    cnt = 0
    for n in range(10000):
        if isLychrel(n):
            cnt += 1
    print(cnt)

main()