import math
t=input()
while t:
        a=map(float,raw_input().split())
        s=(a[0]+a[1]+a[2]+a[3])/2
        print math.pow((s-a[0])*(s-a[1])*(s-a[2])*(s-a[3]),0.5)
        t-=1





