for i in range(input()):
        a = map(int,raw_input().split())
        b = map(int,raw_input().split())
        str = ""
        flag = True
        for j in range(a[0]):
                if j%2:
                        flag = True
                else:
                        flag = False
                for k in range(b[0]):
                        if j%2:
                                flag = True
                        else:
                                flag = False
                        for l in range(a[1]):
                                flag = not flag
                                for m in range(b[1]):
                                        if flag:
                                                str += "X"
                                        else:
                                                str += "."
                        print str
			str = ""

