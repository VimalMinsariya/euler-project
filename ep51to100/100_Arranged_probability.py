x, y = 1, 1
n, m = (x+1)//2, (y+1)//2
line = 10**12
while m <= line:
    x, y = 3*x + 2*y, 4*x + 3*y
    n, m = (x+1)//2, (y+1)//2

print(m, n)
