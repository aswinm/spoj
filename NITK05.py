for i in range(input()):
	n,k = map(int,raw_input().split())
	v = map(int,raw_input().split())
	f = map(int,raw_input().split())
	v.sort()
	f.sort()
	fl = 0
	for j in range(n):
		if v[j]+f[n-j-1]<k:
			fl = 1
			break
	if not fl:
		print "YES"
	else:
		print "NO"
