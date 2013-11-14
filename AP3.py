test=input()
while test>0:
	x,y,s = map(int,raw_input().split())
	a=x+y
	b=(-7*x)+(-5*y)-(2*s)
	c=12*s
	n=(-1*b)+((b*b)-(4*a*c))**(.5)
	n=int(n/(2*a))
	print n
	d=int((y-x)/(n-6))
	first=x-(2*d)
	i=0
	for i in range(int(n)):
		print first+(i*d),
	test=test-1
