d = {}
def numser(n):
	if n <= 4:
		return n
	else:
		if n in d.keys():
			return d[n]
		x =  numser(n-3)+numser(n-1)
		d[n] = x
		print x 
		return x
		
for i in range(1,5):
	print i
numser(100)

