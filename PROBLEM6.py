for i in range(input()):
	a,b = map(int,raw_input().split())
	m = 1
	for j in  range(a,b,-1):
		m *= j
	print m
