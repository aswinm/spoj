while True:
        try:
                n=int(raw_input())
        except:
                break
        a=raw_input()
        b=raw_input()
        i=0
        k=0
        while i<len(b):
                x=b.find(a,i)
                if x>0:
                        print x
                        k=1
                        i=x
                i+=1
        print ""
        if k==0:
                print ""


