for i in range(input()):
	n = input()
	n-=1
	m = n/5
	x = n/3
	p = n/15
	m = (m*(m+1)/2)*5
	x = (x*(x+1)/2)*3
	p = (p*(p+1)/2)*15
	print m+x-p

