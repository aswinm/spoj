for i in range(input()):
	n = input()	
	y = range(1,n+1)
	z = int(n**0.5)
	f = 1
	for j in range(2,z+1):
		for k in range(n):
			if y[k]!= j and y[k]%j == 0:
				y[k] = 0
	for k in range(n):
		if y[k] != 0:
			f = 0
			print y[k]
	print ""
	if f:
		print ""
	

