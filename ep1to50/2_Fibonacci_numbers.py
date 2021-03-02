f1, f2, f3 = 1, 1, 2
sum = 0
while f3 < 4*10**6+1:
    if f3%2 == 0:
        sum += f3
    f2, f1 = f3, f2
    f3 = f2 + f1

print(sum)