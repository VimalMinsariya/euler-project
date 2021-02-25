import math

def ratio(n):
    t = (n*math.sqrt(2*n)-n+1)/(n**2 + 1)
    theta = math.asin(t)
    dif = (n**2-1-(n-1)*math.sqrt(2*n))/(n**2+1)
    result = 2*(1-theta-dif)/(4-math.pi)
    return result

n = 1
while ratio(n) > 0.001:
    print(ratio(n))
    n += 1

print(n, ratio(n))