def ror(s,i):
    for x in range(i):
        s=s[-1]+s[0:len(s)-1]
    print s
    
ror("10001",2)