x = ['0','6','9']
for i in range(input()):
	y = raw_input()
	c = 0
	for j in y:
		if j == '8':
			c += 2
		elif j in x:
			c += 1
	print c

