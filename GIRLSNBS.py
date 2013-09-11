while True:
	x = map(int,raw_input().split())
	if x[0]==-1 and x[1] == -1:
		break
	print (x[0]+x[1])/(min(x[0],x[1])+1)

