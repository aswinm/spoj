for i in range(input()):
	x = map(int,raw_input().split())
	y = map(int,raw_input().split())
	y.sort()
	diff = y[x[1]-1] - y[0]
	for j in range(1,x[0]-x[1]+1):
		diff = min(diff,y[j+x[1]-1]-y[j])
	print diff


