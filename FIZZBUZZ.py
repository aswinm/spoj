for i in range(input()):
	n = input()
	x = n%5
	y = n%7
	if y==0 and x == 0:
		print "fizzbuzz"
	elif y==0:
		print "buzz"
	elif x == 0:
		print "fizz"
	else:
		print n

