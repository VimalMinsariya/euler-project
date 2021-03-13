f0, f1, f2, f3 = 1, 1, 2, 4

for i in range(4,51):
    f0, f1, f2, f3 = f1, f2, f3, f0+f1+f2+f3

print(f3)