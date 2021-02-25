array=[1,2,3,4,5,6,7]
data = enumerate([1, 2, 3])
print(data, type(data))

for i, value in data:
    print(i, ":", value)
print()