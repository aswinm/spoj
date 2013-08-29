while True:
	n = input()
	if not n:
		break
	m = map(int,raw_input().split())
	print max(m)
