from fractions import gcd
t=input()
i=0
while i<t:
        num=raw_input()
        n=float(num)
        l = 0
        p = 0
        d = 1
        for j in range(len(num)):
             	if p:
             		d *= 10     	  
        	if num[j]== '.':
             		p = 1
             	else:
             		l = l*10 + int(num[j])
        print int(d/gcd(l,d))
        i+=1



