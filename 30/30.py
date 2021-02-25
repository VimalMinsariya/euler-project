def sumOffifth(n):
    a=str(n)
    sum=0
    for i in a:
        sum += int(i)**5
    return sum

i=2
sum=0
while i<10**6:
    if i == sumOffifth(i):
        sum += i
        print(i)
    i += 1
print("sum: ",sum)