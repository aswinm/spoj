while 1:
    a,b=raw_input().split()
    if a=='*' and b=='*':
	break
    m=len(a)
    n=len(b)
    if m<n:
	a=(n-m)* '0'+a
    elif n<m:
	b= (m-n)*'0'+b           
    if a>b:
	print ">"
    elif a==b:
	print "="
    else:
	print "<"             
