'''regFile = list(range(31))
print regFile
del regFile[0]
print regFile
regFile.insert(0,100)
print regFile
'''

'''def MOVE_IMMEDIATE(binary):
    return {
       111 : pr(),
       000 : pr(),
       001 : pr(),
    }[binary]
'''

def pr():
    print "hii"
def pr2():
    print "hii2"
def pr3():
    print "hii3"


    
MOV={ 1 : pr,
       0 : pr2,
       2 : pr3,}

MOV[0]()

print bin(-2)[2:].zfill(32)

