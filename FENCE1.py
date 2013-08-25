from math import acos
while True:
        n=input()
        if n==0:
                break
        r=n/(4*acos(0))
        a=4*r*r*acos(0)
        print "%.2f" %a


