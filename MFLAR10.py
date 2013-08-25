while True:
        a=raw_input()
        if a=='*':
                break
        a=a.split()
        c=a[0][0].lower()
        flag=0
        for i in range(1,len(a)):
                if a[i][0].lower()!=c:
                        flag=1
        if flag==0:
                print "Y"
        else:
                print "N"
                

