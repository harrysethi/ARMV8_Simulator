def asr(s,i):
    s=s[0]*i+s[0:len(s)-i]
    print s
    
asr("10001",1)