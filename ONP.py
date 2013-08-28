for i in range(input()):
	x = raw_input()
	s = ""
	op = []
	for j in x:
		if j >='a' and j <= 'z':
			s+= j
		elif j == ')':
			s+= op.pop()
		elif j != '(':
			op.append(j)
	print s

