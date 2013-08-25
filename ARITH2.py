t=input()
while t:
    t-=1
    raw_input()
    x=raw_input().split()
    while len(x)>=3:
        if x[1]=='*':
            m=int(x[0])*int(x[2])
        elif x[1]=='+':
            m=int(x[0])+int(x[2])
        elif x[1]=='/':
            m=int(x[0])/int(x[2])
        else:
            m=int(x[0])-int(x[2])
        del x[0]
        del x[0]
        x[0]=str(m)
    print x[0]











