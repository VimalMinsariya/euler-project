import time
start=time.time()

op=[3,5,7]
oc=[]
isg = True
n=9

def isgc(n):
	d= False
	k=1
	j=1
	for i in op:
		t=((n-i)/2)**(1/2)
		if t==int(t):
			d=True
			k=i
			j=t
	return [d,k,int(j)]
	
while isg:
	i=3
	isprime = True
	while i<=n**(1/2):
		if n%i == 0:
			oc.append(n)
			isprime = False
			isg=isgc(n)[0]
			if isg==False:
				print(n)
			else:
				print(n,isgc(n)[1], isgc(n)[2])
			break
		i += 2
	if isprime == True:
		op.append(n)
	n += 2

print(time.time()-start)
