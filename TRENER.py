x = [0]*26
for i in range(input()):
	y = raw_input()
	x[ord(y[0])-97]+= 1
s = ""
for j in range(26):
	if x[j]>=5:
		s += chr(97+j)
		f = 0
if not s:
	print "PREDAJA"
else:
	print s
