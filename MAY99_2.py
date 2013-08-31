d = { 1:'m', 2:'a',3: 'n' , 4: 'k', 0: 'u'}
for i in range(input()):
	x = input()
	s = ""
	while x:
		x,r = divmod(x,5)
		if r == 0:
			x -= 1
		s = d[r] + s
	print s

