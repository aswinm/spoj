
for i in range(input()):

	a,b = map(int,raw_input().split())
	s = 0
	l = len(str(a))
	x = a-1
	m = 10**9+7
	com = int("9"*l)
	if com>b:
		com = b
	f = 1
	while com<=b and f:
		s += (((com*(com+1)/2)-(x*(x+1)/2))*l)%m
		x = com
		com = com*10 + 9
		if com>b:
			com = b
			f = 0
		l += 1
	if not f:
		s += (((com*(com+1)/2)-(x*(x+1)/2))*l)%m
	print s%m 








