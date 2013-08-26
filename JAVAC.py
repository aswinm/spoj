while True:
	try:
		a=raw_input()
        	str=""
		flag = 1
        	if a=="":
        	        break
		if a[0] == '_':
			print "Error!"
			continue
		if a == a.lower() and '_' not in a:
			print a
			continue
        	if a!=a.lower():
			if len(a) == 1 or '_' in a:
        	        	print "Error!"
        	        	continue
			if a[0] != a[0].lower():
				print "Error!"
				continue
		if a == a.lower():
			if len(a)==1:
				print a
			elif '_' not in a or a[-1] == '_':
				print "Error!"
				continue
        	if a!=a.lower():
        	        for i in range(len(a)):
        	                if a[i]!=a[i].lower():
        	                        str+='_'+a[i].lower()
        	                else:
        	                        str+=a[i]
        	else:
        	        i=0
        	        while i<len(a):
        	                if a[i] != '_':
        	                        str+=a[i]
        	                        i+=1
        	                else:
					if a[i+1] == '_':
						flag = 0
						print "Error!"
						break
        	                        str+=a[i+1].upper()
					i+=2
		if flag:
        		print str
		else:
			flag = 1
	except:
		break	
	





