d = {}
def val(n):
	if n<12:
		return n
	elif n in d.keys():
		return d[n]
	x =  val(n/2) + val(n/3) + val(n/4)
	d[n] = x
	return x

while True:
	try:
		n = input()
	except:
		break
	print val(n)
