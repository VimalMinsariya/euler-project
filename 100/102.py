import time
start = time.time()

def orientation(A,B):
    ax,ay = tuple(A)
    bx,by = tuple(B)
    k = ax*by - bx*ay
    if k<0:
        return -1
    elif k>0:
        return 1
    else:
        return 0

def containO(P,Q,R):
    k = orientation(P,Q) + orientation(Q,R) + orientation(R,P)
    return k

A,B,C = [-340,495], [-153,-910], [835,-947]
X,Y,Z = [-175,41], [-421,-714], [574,-645]

assert containO(A,B,C) in [-3,3]
assert containO(X,Y,Z) not in [-3,3]

cnt = 0
point3 = open('p102_triangles.txt').readlines()
for s in point3:
    points = s.split(',')
    A,B,C = [int(points[0]), int(points[1])], [int(points[2]), int(points[3])], [int(points[4]), int(points[5])]
    if containO(A,B,C) in [-3,3]:
        cnt += 1

print(cnt)

print(time.time()-start)