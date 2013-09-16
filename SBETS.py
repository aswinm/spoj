for i in range(input()):
	win = []
	lost = []
	for j in range(16):
		x = raw_input().split()
		if x[2]<x[3]:
			win.append(x[1])
			lost.append(x[0])
		else:
			win.append(x[0])
			lost.append(x[1])
	y = set(win)-set(lost)
	for i in y:
		print i
			

