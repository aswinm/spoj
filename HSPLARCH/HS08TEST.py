x = map(float,raw_input().split())
if x[0]%5!=0:
	print "%.2f"%(x[1])
elif x[1]-x[0]<0.5:
	print "%.2f"%(x[1])
else:
	print "%.2f"%(x[1]-x[0]-0.5)
