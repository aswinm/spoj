for i in range(input()):
	a = [1,2,3,4,5,6,7,8,9,10]
	x = map(int,raw_input().split())
	x[1] -= 1
	while x[1]:
		x[1] -= 1
		for j in range(1,10):
			a[j] += a[j-1]
	print x[0],a[9]
