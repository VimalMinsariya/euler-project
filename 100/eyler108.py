S=[7,8,9,11,14]
n=len(S)
s=0

for i in range(0,3**n):
	q=i/3
	r=i%3
	s=s+S[0]*(r-1)
	wp=[r-1]
	for j in range(0,n-1):
		r=q%3
		wp.append(r-1)
		s=s+S[j+1]*(r-1)
		q=q/3
	print wp,s
	s=0