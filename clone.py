while True:
	a = map(int,raw_input().split())
	if a[0] == 0 and a[1] == 0:
		break
	lis = []
	dic =[0]*a[0] 
	for i in range(a[0]):
		b = raw_input()
		if b in lis:
			dic[lis.index(b)] += 1		
		else:
			lis.append(b)
			dic[lis.index(b)] = 1
	for i in range(1,a[0]+1):
		print dic.count(i)
	
