import time
start = time.time()

def phi_1_to_n(n,k):
    phi=[None]*(n+1)
    phi[0] = 0;
    phi[1] = 0;
    for i in range(2,n+1):
      phi[i] = int((i-1)*k)
    for i in range(2,n+1):
      j = 2*i
      while j <= n:
        phi[j] -= phi[i]
        j += i
    return phi

N=12000
p = phi_1_to_n(N,1/2)
q = phi_1_to_n(N,1/3)
print(sum(p[2:])-sum(q[2:])-1)

print(time.time()-start)