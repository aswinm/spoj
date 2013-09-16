
while True:
        a,b,c=map(int,raw_input().split())
        if a!=0 or b!=0 or c!=0:
                if (b-a)==(c-b):
                        d=c+b-a
                        print "AP",d
                else:
                        d=c*b/a
                        print "GP",d
        else:
		break
