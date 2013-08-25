i=0
while i==0:
        a,b,c=raw_input().split()
        a=int(a)
        b=int(b)
        c=int(c)
        if a!=0 or b!=0 or c!=0:
                if (b-a)==(c-b):
                        d=c+b-a
                        print "AP",d
                else:
                        d=c*b/a
                        print "GP",d
        else:
                i=1
