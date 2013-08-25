i=input()
j=0
while j<i:
        a,c=raw_input().split()
        a=int(a)
        c=int(c)
        b=0
        while a>0:
                b=b*10+a%10
                a=a/10

        d=0
        while c>0:
                d=d*10+c%10
                c=c/10
        e=b+d
        f=0
        while e>0:
                f=f*10+e%10
                e=e/10
        j=j+1
        print f


