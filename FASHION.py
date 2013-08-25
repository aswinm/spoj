t=input()
i=0
def array(a,c,j):
        k=0
        while k<j:
                if a[k]!=" ":
                        c.append(int(a[k]))
                k+=1

while i<t:
        j=input()
        a=raw_input().split()
        c=[]
        b=raw_input().split()
        d=[]
        array(a,c,j)
        c.sort()
        array(b,d,j)
        d.sort()
        k=0
        m=0
        while k<j:
                m+=c[k]*d[k]
                k+=1
        print m
        i+=1


