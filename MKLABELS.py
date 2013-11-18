i = 1
while True:
	n = input()
	if not n:
		break
	y = n**(n-2)
	print "Case %d, N = %d, # of different labelings = %d"%(i,n,y)
	i += 1
