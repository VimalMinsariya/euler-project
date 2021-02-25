length = 0
length_max = 0

#for M in range(1,1001):
M=31
N=1
i=0

remainder = [N%M]
deci = [N/M]

while(True):
	k = remainder[i] * 10
	a = k % M
	b = k / M
	if(a in remainder):
		remainder.append(a)
		deci.append(b)
		pos = remainder.index(a)
		length = i - pos + 1
		break
	remainder.append(a)
	deci.append(b)
	i=i+1

decistr = str(deci[0])+'.'

for j in range(1,i+2) :
	if(j == pos + 1) :
		decistr = decistr + '(' + str(deci[j])
	else:
		decistr = decistr + str(deci[j])	
decistr = decistr + ')'

#if(length > length_max):
print '1/' + str(M) + ' = ' + decistr
print 'length = ', length
length_max = length
