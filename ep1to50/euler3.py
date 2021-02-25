import math

test=600851475143
k=1000000
num=[1]
for i in range(1,k+1):
	num.append(i)
	

n=1
t=1
p=[1]
while(n<k):
	j=1
	if(num[n] != 1):
		p.append(num[n])
		while(j*n<=k):
			num[j*n]=1
			j=j+1		
		t=t+1
	n=n+1

for i in p:
	if(test%i == 0):
		print i
