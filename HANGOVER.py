while True:
	a = input()
	if a== 0.0:
		break
	sum = 0
	j = 1
	while True:
		sum += 1.0/(j+1)
		if sum>=a:
			print j, "card(s)"
			sum = 0
			break
			j=1
		j+=1

