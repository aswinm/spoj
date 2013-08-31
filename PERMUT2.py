while True:
	n = input()
	if n==0:
		break
	x = ma(int,raw_input().split())	
	flag = 0
	for i in range(1,len(x)+1):
		if i != (x[x[i-1]-1]):
			flag = 1
			break
	if flag == 0:
		print "ambiguous"
	else:
		print "not ambiguous"
