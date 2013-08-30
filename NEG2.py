def func(n):
	val = ""
	if not n:
		return "0"
	while n!=0:
		n,remainder = divmod(n,-2)
		if remainder<0:
			n += 1
			remainder += 2
		val = str(remainder) + val
	return val
print func(input())
