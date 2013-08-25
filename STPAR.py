while True:
	x = input()
	if x == 0:
		break
	min = 1
	a = map(int,raw_input().split())
	lis = []
	i = 0
	while i < x:
		if a[i]>min:
			lis.append(a[i])
			i += 1
		else:
			min += 1
			i += 1
		while lis:
			if lis[-1]>min:
				break
			lis.pop()
			min += 1
	for j in lis:
		if lis[-1] == min:
			lis.pop()
			min += 1
				
	if not lis :
		print "yes"
	else:
		print "no"
		





		
