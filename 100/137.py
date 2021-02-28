sol1 = {0:(1,1), 1:(2,4)}
sol = {}
nugget = 0
t = 2
while nugget < 15:
    x1, y1 = sol1[t-2]
    x2, y2 = sol1[t-1]
    sol1[t] = (3*x2-x1, 3*y2-y1)
    if sol1[t][1]%5 == 1:
        nugget += 1
        sol[nugget] = sol1[t]
    t += 1

N = (sol[15][1]-1)//5
S = sol[15][0]
x = (S-1)/(2*N) - 0.5
print(N, x)
