for i in range(1,input()+1):
	n,p = map(int,raw_input().split())
	ps = [0]*p
	p0 = 1
	pp = 1
	pk = 1
	
	for j in range(n):
		x = map(int,raw_input().split())
		for k in range(len(x)):
			if x[k]:
				ps[k] += 1
		if sum(x)==0:
			p0 = 0
		if sum(x)==p:
			pp = 0
	for j in ps:
		if j==0:
			pk = 0
			break
	s = "" +str(pk)+str(p0)+str(pp)
	print "Case %d:"%(i),int(s,2)
	
