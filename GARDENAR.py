for i in range(input()):
	a,b,c = map(int,raw_input().split())
	x = 3**.5
	s = (a+b+c)/2.0
	S = ((a**2)+(b**2)+(c**2))*x/4.0
	S += ((s*(s-a)*(s-b)*(s-c))**0.5)*3.0
	print "%.2f"%(S/2.0)
