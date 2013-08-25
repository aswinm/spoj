t=input()
i=0
while i<t:
        a=raw_input().split(" ")
        a=map(int,a)
        if a[0]==0 and a[1]==0:
                print '1'
        elif a[1]==0:
                print '1'
        else:
                c=a[1]%4
                if c==0:
                        c=4
                d=1
                for j in range(1,c+1):
                        d*=a[0]
                print d%10
        i+=1


