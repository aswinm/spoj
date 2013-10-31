for i in range(input()):
	x = "".join(raw_input().split())
	ns = 0
	ds = 0
	i = 0
	l = len(x)
	while ds<6 and ns<6:
		d = 0
		n = 0
		while d!=4 and n != 4 and i<l:
			if x[i]=='N':
				n += 1
			else:
				d += 1
			i += 1
		if abs(d-n)<=2:
			while abs(d-n)<2 and i<l:
				if x[i] == 'N':
					n += 1
				else:
					d += 1
				i += 1
		if n<d:
			ds += 1
		else:
			ns += 1
	while  abs(ns-ds)==1 and i<l:
		n = 0
		d = 0
		while d!=4 and n!=4 and i<l:
			if x[i] == 'N':
				n += 1
			else:
				d += 1
			i += 1
		if abs(d-n)<=2:
			while abs(d-n)<2:
				if x[i] == 'N':
					n += 1
				else:
					d += 1
				i +=1
		if n>d:
			ns += 1
		else:
			ds += 1

	if ns == 6 and ds == 6:
		d = 0
		n = 0	
		while i<l:
			if x[i] == 'N':
				n+= 1
			else:
				d += 1
			i += 1
		if d>n:
			ds += 1
			print "D %d (%d-%d)"%(ds,d,n)
			print "N %d"%(ns)
		else:
			ns += 1
			print "N %d (%d-%d)"%(ns,n,d)
			print "D %d"%(ds)
	else:
		if ns>ds:
			print "N %d"%(ns)
			print "D %d"%(ds)
		else:
			print "D %d"%(ds)
			print "N %d"%(ns)










