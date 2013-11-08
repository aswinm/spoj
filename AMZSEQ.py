lis = [0]*25
lis[0] = 1
lis[1] = 3
for i in range(2,25):
	lis[i] = 2*lis[i-1]+lis[i-2]
print lis[input()]
