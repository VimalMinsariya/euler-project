def vec(P,Q):
    px, py = tuple(P)
    qx, qy = tuple(Q)
    return [qx-px,qy-py]

def dot_product(P,Q):
    px, py = tuple(P)
    qx, qy = tuple(Q)
    k = px*qx + py*qy
    return k

def length(P,Q):
    v = vec(P,Q)
    l = dot_product(v,v)
    return l**(1/2)
assert length([1,2],[4,6]) == 5

def cos_angle(S,P,R):
    a = dot_product(vec(P,S),vec(P,R))
    b = length(P,S)*length(P,R)
    return a/b

K = 5*(7500**2)

t = int(2500*(5**(1/2)))+1
test = True
while test:
    P = [0,t]
    x = (K-9*(K/(9*t))**2)/5
    S = [-x,K/(9*t)]
    R = [x,K/(9*t)]
    print(S,P,R,cos_angle(S,P,R))
    if cos_angle(S,P,R) >= (1/2)**(1/2):
        test = False
    t += 100000
print(t-2)



