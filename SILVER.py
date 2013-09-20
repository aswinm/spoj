while True:
	n = input()
	if n==0:
		break
	print len(bin(n))-3
