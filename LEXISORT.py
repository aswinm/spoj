for i in range(input()):
	x = input()
	li = []
	for j in range(x):
		li.append(raw_input())
	li.sort()
	for j in li:
		print j
