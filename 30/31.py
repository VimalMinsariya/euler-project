import time
start=time.time()

def main0():
    def total(a,b,c,d,e,f):
        return 100*a+50*b+20*c+10*d+5*e+2*f

    s=0

    for a in range(3):
        for b in range(5):
            for c in range(11):
                for d in range(21):
                    for e in range(41):
                        for f in range(101):
                            if total(a,b,c,d,e,f)<=200:
                                s += 1

    print(s)

def main1():
    def compute(coins: list, n: int) -> int:
        combinations = [1] + [0] * n
        for i in range(len(coins)):
            for j in range(coins[i], n + 1):
                combinations[j] += combinations[j - coins[i]]
        return combinations[-1]

    coin_list = [1, 2, 5, 10, 20, 50, 100, 200]

    print(compute(coin_list, 200))

def main2():
    coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
    charateristicf = {1: [1, -1]}
    a = [1,1]
    n = 2
    p = 1
    money = 200 # int(input('money: '))
    while n < money + 1:
        if n == coin_list[p]:
            f = charateristicf[coin_list[p-1]]
            x1 = f + [0] * n
            x2 = [0] * n + f
            result = []
            for j in range(len(x1)):
                result.append(x1[j] - x2[j])
            charateristicf[n] = result
            if p < len(coin_list)-1:
                p += 1
        t = 0
        l = charateristicf[coin_list[p-1]]
        for j in range(1, len(l)):
            if n >= j:
                t -= l[j] * a[n - j]
            else:
                break
        a.append(t)
        n += 1
    print(t)

main0()

print("Elapsed Time: ",time.time()-start)