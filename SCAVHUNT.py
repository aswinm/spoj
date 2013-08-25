t=input()
l=1
while l<=t:
        n=input()
        dic={}
        source=[]
        dest=[]
        for i in range(n-1):
                x=raw_input().split()
                dic[x[0]]=x[1]
                source.append(x[0])
                dest.append(x[1])
        print "Scenario #%d:" %(l)
        s=list(set(source)-set(dest))[0]
        print s
        for i in range(n-1):
                print dic[s]
                s=dic[s]
        print ""
        l+=1


