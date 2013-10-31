i = 1
while True:
	try:
		a = map(int,raw_input().split())
	except:
		break
	if not a:
		break
	a.sort()
	print "Case %d:"%(i),
	print a[2]+a[3]
	i += 1
