x = []
for i in range(10):
	x.append(input())
a = abs(100-x[0])
su = x[0] 
val =su 
i =1 
while i<10:
	su += x[i]
	b = abs(su-100)
	if b>a:
		print val 
		break
	else:
		val = su
		a = b
	i += 1
if i == 10:
	print val
	 
