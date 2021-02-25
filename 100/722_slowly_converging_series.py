def f(n):
    value = (n**15) * ((1-1/(2**25))**n)
    return value

sum = 0
for i in range(1,1000001):
    sum += f(i)
    print(i, sum)




