for i in range(input()):
	x = input()
	c = 0
	for j in range(x):
		y = raw_input()
		if y == 'lxh':
			c += 1
	if c%2:
		print 'lxh'
	else:
		print 'hhb'
