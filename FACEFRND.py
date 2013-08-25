t=input()
arr=[]
frnd=[]
while t:
        a=raw_input().split()
        frnd.append(a[0])
        del a[0],a[0]
        arr.extend(a)
        t-=1
print len(set(arr)-set(frnd))


