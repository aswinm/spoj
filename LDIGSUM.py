for i in range(input()):
	x = map(int,list(raw_input()))
	if len(x)<2:
		print x
		continue
	while len(x)>1:
		s = sum(x)
		x = map(int,list(str(s)))
	print s
		
