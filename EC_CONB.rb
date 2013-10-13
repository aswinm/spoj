num = gets()
num = (num.to_i)-1
for i in (0..num)
	x = gets()
	x = x.to_i
	if x%2>0
		puts(x)
	else
		x =  x.to_s(2).reverse
		puts(x.to_i(2))
	end
	num -= 1
end
