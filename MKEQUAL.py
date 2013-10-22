for i in range(input()):
	n = input()
	x = map(int,raw_input().split())
	if x%n:
		print n-1
	else:
		print n
