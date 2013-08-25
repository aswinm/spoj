while True:
        n=input()
        if n==0:
                break
        arr=[]
        i=n
        while n>0:
                x=input()
                arr.append(x)
                n-=1
        arr.sort()
        flag=0
        for j in range(0,i-1):
                if (arr[j+1]-arr[j])>200:
                        flag=1
        ret=1422-arr[-1]
        if ret>100:
                flag=1
        if flag==0:
                print "POSSIBLE"
	else:
		print "IMPOSSIBLE"


