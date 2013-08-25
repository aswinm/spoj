while True:
        a=map(int,raw_input().split())

        if a[0]==0 and a[1]==0:
                break
        at=map(int,raw_input().split())
        de=map(int,raw_input().split())
        at.sort()
        de.sort()
        if at[0]<de[1]:
                print "Y"
        else:
                print "N"

