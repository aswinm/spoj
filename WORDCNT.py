for i in range(input()):
        a=raw_input().split()
        if not  a:
                print 0
                continue
        max=1
        y=1
        for j in range(1,len(a)):
                if len(a[j-1])==len(a[j]):
                        y+=1
                else:
                        if y>max:
                                max=y
                        y=1
        if y>max:
                max=y
        print max


