a=input()
def convert(a):
        i=0
        while a>0:
                if a%2:
                        i+=1
                a=a/2
        return i
c=convert(a)
if c==1:
        print "TAK"
else:
        print "NIE"


