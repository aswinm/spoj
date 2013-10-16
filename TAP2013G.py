n = input()
x = map(int,raw_input().split())
y = map(int,raw_input().split())
x.sort()
y.sort()
j = n-1
k = n-1
c = 0
while j>=0 and k>=0:
	if y[j]>x[k]:
		c += 1
		j -= 1
		k -= 1
	else:
		k -= 1


print c
