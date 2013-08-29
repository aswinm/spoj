for i in range(input()):
	n = input()
	x = map(int,raw_input().split())
	k =0
	x.sort()
	count = 0
	while k<len(x):
		if x[k]*2 in x and x[k]!=0:
			x[x.index(x[k]*2)] = 0
			x[k] = 0
			count += 1
		k += 1
	print count
