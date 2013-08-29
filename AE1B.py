n = map(int,raw_input().split())
x = map(int,raw_input().split())
x.sort()
x.reverse()
ans = 0
tot = n[1]*n[2]
for i in range(n[0]):
	ans += x[i] 
	if ans>=tot:
		print i+1
		break


