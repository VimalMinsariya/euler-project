sol1 = [(7, 1), (8, 2), (13, 5), (17, 7), (32, 14), (43, 19)]
sol = {1:(17,7), 2:(32,14)}
nugget = 2
print(sol1[0])
while nugget < 30:
    for i in range(6):
        x, y = sol1[i]
        sol1[i] = (9*x+20*y, 4*x+9*y)
        if sol1[i][0] % 5 == 2:
            nugget += 1
            sol[nugget] = sol1[i]

print((sol[20][0]-7)//5)
result = 0
for i in range(1,31):
    result += (sol[i][0] - 7)//5
print(result)