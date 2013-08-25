t=input()
l=1
while l<=t:
        input()
        a=map(int,raw_input().split())
        sum=0
        count=0
        for i in a:
        	sum+=i
                if sum<=0:
                	count-=(sum)
                        sum=0
        print "Scenario #%d: %d" % (l, count+1)
        l+=1











