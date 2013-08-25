i=input()
while i:
        a,b=raw_input().split()
        a=int(a)
        b=int(b)
        c=a-b
        if (c==0 or c==2):
                if a%2:
                        print a+b-1
                else:
                        print a+b
        else:
                print "No Number"

        i-=1



