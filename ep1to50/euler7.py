# coding: utf-8
import math
from pylab import *

p=[2]
n=1
pt=3
sum=2
while(pt<2000000):
	srtp=math.sqrt(pt)
	i=0
#	scatter(pt,n,s=120,c='#64c2ff')
	while(p[i] <= srtp):
		if(pt%p[i] == 0):
			pt=pt+1
			break
		i=i+1
	if(p[i] > srtp):
		p.append(pt)
		sum=sum+pt
		pt=pt+1
		n=n+1
print(sum)	
#print(n,p[-1])

xlabel('n')
ylabel('the number of prime less than n')
title('Distribution of prime')
grid(True)
show()
#savefig('distribution_of_prime100.png',dpi=300)
