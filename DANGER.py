from math import log
while True:
        n=int(input())
        if n==0:
                break
        print  2*(n - 2**(int(log(n,2))))+1

