import time
start=time.time()

spiral=[[0,0],[1,0]]

def forward(v,w):
    return [2*w[0]-v[0],2*w[1]-v[1]]

def turnRight(v,w):
    return [w[0]+w[1]-v[1],w[1]-w[0]+v[0]]

i=2
sum=1
test1 = 1
test2 = 1

while i<1001*1001:
    a = turnRight(spiral[i-2],spiral[i-1])
    b = forward(spiral[i-2],spiral[i-1])
    if spiral[i-1][0] > 0 and test2 == 1:
        spiral.append(a)
    elif test1 == 0:
        spiral.append(a)
    elif spiral[i-1][0] < 0 and test2==0:
        spiral.append(a)
    else:
        spiral.append(b)
    test1 = spiral[-1][0] + spiral[-1][1]
    test2 = spiral[-1][0] - spiral[-1][1]
    if test1 == 0 or test2 == 0:
        sum += (i+1)
    i += 1

print(sum)

print("Elapsed Time: ",time.time()-start)