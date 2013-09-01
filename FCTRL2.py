dic = {}
def fact(n):
	if n==1:
		return 1
	elif n in dic.keys():
		return dic[n]
	else:
	 	x = n*fact(n-1)
	 	dic[n] = x
	 	return x
for i in range(input()):
	print fact(input())	







