x = raw_input()
d = 0.0
while True:
	try:
		y = raw_input()
	except:
		break
	a = map(float,x[x.index('(')+1:x.index(')')].split(','))
	b = map(float,y[y.index('(')+1:y.index(')')].split(','))
	d += (((a[0]-b[0])**2)+(b[1]-a[1])**2)**0.5
	print "The salesman has traveled a total of %.3f kilometers"%(d)
	x =y
	
