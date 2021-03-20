import math

def vec(A,B):
    x1, y1 = A
    x2, y2 = B
    x, y = x2 - x1, y2 - y1
    return (x,y)

def dotproduct(A,B):
    x1, y1 = A
    x2, y2 = B
    return x1*x2+y1*y2

def norm(P):
    x, y = P
    return x**2 + y**2

def angle(P,A,Q):
    AP, AQ = vec(A,P), vec(A,Q)
    a = math.sqrt(norm(AP))
    b = math.sqrt(norm(AQ))
    k = dotproduct(AP,AQ) / (a*b)
    return k

def solve_qudratic(co):
    a, b, c = co
    D = b**2 - 4*a*c
    re1 = (-b + math.sqrt(D))/(2*a)
    re2 = (-b - math.sqrt(D))/(2*a)
    return (re1,re2)

def ratio(P):
    x, y = P
    return (x/2500,y/2500)

def solve_tp(P):
    r, s = P
    if r == 0 and s != 0:
        y = 5/s
        x0 = math.sqrt((45-9*y**2)/5)
        x1 = -x0
        return ((x0,y),(x1,y))
    elif r !=0 and s == 0:
        x = 9/r
        y0 = math.sqrt((45-5*x**2)/9)
        y1 = -y0
        return ((x,y0),(x,y1))
    else:
        a = 25*r**2 + 45*s**2
        b = -450*r
        c = 2025-405*s**2
        x = solve_qudratic((a,b,c))
        x0, x1 = x[0], x[1]
        y0, y1 = (45-5*r*x0)/(9*s), (45-5*r*x1)/(9*s)
        return ((x0,y0),(x1,y1))

def angle_tl(P):
    T1, T2 = solve_tp(P)
    return angle(T1,P,T2)

def isInEllipse(P):
    x,y = P
    d = 5*(x**2)+9*(y**2) - 45
    if d <= 0 : return True
    return False

def cntl(P):
    a, b = P
    if b == 0:
        k = 4
    else:
        k = 2
    P = ratio((a,b))
    cnt = 0
    while isInEllipse(P):
        b += 1
        P = ratio((a,b))
    while angle_tl(P) < limit:
        cnt += 1
        b += 1
        P = ratio((a,b))
    return k*cnt

limit = math.cos(math.radians(45))
a = 1
P = (a,0)
t = cntl((0,1))
print(810861106+t-cntl((1,0)))
while isInEllipse(ratio(P)):
    t += cntl(P)
    a += 1
    P = (a,0)
while angle_tl(ratio(P)) < limit:
    t += cntl(P)-2
    a += 1
    P = (a,0)

print(t,a-1)
print(limit, angle_tl((7,0)))
