while True:
	n = input()
	x = []
	s = 0
	if n==-1:
		break
	for i in range(n):
		
		x.append(input())
		s += x[-1]
	if s%n != 0:
		print "-1"
	else:
		s = s/n
		c = 0
		for i in x:
			if i<s:
				c += s-i
		print c


