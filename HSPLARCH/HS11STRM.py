for i in range(input()):
	x = raw_input().split()
	m = list(x[0])
	for j in x[1]:
		if j in m:
			del m[m.index(j)]
	s = ""
	for j in m:
		s += j
	print s
