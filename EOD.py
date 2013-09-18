def count(x):
	odd =0 
	even = 0
	while x:
		n = x%10
		if (n&1):
			odd += 1
		else:
			even += 1
		x /= 10
	return odd,even

for i in range(input()):
	odd,even = count(input())
	print "odd" if odd>even else "even"
