for i in range(input()):
	n = input()
	x = map(int,raw_input().split())
	if sum(x)==n:
		if n%2:
			print "Brother"
		else:
			print "John"
	else:
		a = 0
		for j in x:
			a ^= j
		if a == 0:
			print "Brother"
		else:
			print "John"
