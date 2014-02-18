for i in range(input()):
	s = raw_input()
	m,n = map(int,raw_input().split())
	l = len(s)
	if m==n:
		print l,l
	elif m<n:
		mi = l
		x = 'a'*m
		c = s.count(x)
		ma = c*n + l-c*m
		print mi,ma
	else:
		ma = l
		x = 'a'*m
		c = s.count(x)
		mi = c*n +l -c*m
		print mi,ma
	
