from fractions import gcd
for i in range(input()):
	a,b = map(int,raw_input().split())
	y = gcd(a,b)
	if y == 1:
		print b,a
	else:
		print b/y,a/y
		
	
