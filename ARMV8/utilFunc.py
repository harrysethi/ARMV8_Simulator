'''
@author: harinder
'''
import const
import mem
import armdebug

def hexToBin(s):
    scale = 16  # # equals to hexadecimal    
    binary = bin(int(s, scale))[2:].zfill(const.INST_SIZE)
    return binary

def lsl(s, i):
    return s[i:len(s)] + '0' * i
    
def lsr(s, i):
    return '0' * i + s[0:len(s) - i]
    
def asr(s, i):
    return s[0] * i + s[0:len(s) - i]
    
def ror(s, i):
    for x in range(i):
        s = s[-1] + s[0:len(s) - 1]
    return s

# gives 64 bit, truncate when using
# key should be 0 to 31 in binary string
def getRegValueByStringkey(key):  
    key = int(key, 2)
    assert key >= 0 and key <= 31
    if key != 31:
        return mem.regFile[key]
    else:
        return '0' * 64

def getRegKeyByStringKey(key):
    key = int(key, 2)
    return key

# assuming both s1 and s2 have same length    
def logical_and(s1, s2):
    to_return = ''
    if len(s1) != len(s2):
        print 'Implementation error. Lengths not equal'
        exit(1)
    else:        
        for x in range(len(s1)):
            if s1[x] != s2[x]:
                to_return += '0'
            elif s1[x] == '0':
                to_return += '0'
            else:
                to_return += '1'
    return to_return


def resetInstrFlag():
    const.FLAG_INST_EXECUTED = "0"
    
# sets the register value, prints the inst, sets the instr flag
def finalize(rdKey, val, instr):
    setRegValue(rdKey, val)
    finalize_simple(instr)
    
def finalize_simple(instr):
    print instr
    const.FLAG_INST_EXECUTED = "1"

# val is 64 bit string to be stored in reg with rdkey
def setRegValue(rdKey, val):
    assert rdKey >= 0 and rdKey <= 31
    if(rdKey != 31):
        # ignoring the result - zero register        
        del mem.regFile[rdKey]
        mem.regFile.insert(rdKey, val)
        
# utility function that takes num int convert it into binary of size N
def intToBinary(num, N):
    x = "{0:b}".format(num)
    if(x[0] == '-'):
        x = (x[1:len(x)]).zfill(N)
        return twosComplement(x,N)
    
        
# utility function used by all add-sub instructions
def addSub(op1, op2, sub_op, N, setFlags):
    c_in = '0'
    if(sub_op == '1'):
        op2 = negate(op2)
        c_in = '1'
    unsigned_sum = uInt(op1) + uInt(op2) + uInt(c_in)
    signed_sum = sInt(op1, N) + sInt(op2, N) + uInt(c_in)
    result = ("{0:b}".format(unsigned_sum))
    if(len(result) > N):
        result = result[1:N + 1]
    if(len(result) < N):
        result = result.zfill(N)
    
    # Setting flags
    if(setFlags == '1'):
        if(result[0] == '0'):
            reset_N_flag()
        else:
            set_N_flag()
        if(int(result) == 0):
            set_Z_flag()
        else:
            reset_Z_flag()
        if(uInt(result) == unsigned_sum):
            reset_C_flag()
        else:
            set_C_flag()
        if(sInt(result, N) == signed_sum):
            reset_V_flag()
        else:
            set_V_flag()
    
    return result.zfill(N)

def uInt(x):
    return int(x, 2)

def sInt(x, N):
    result = int(x, 2)
    if(x[0] == '1'):
        result = result - 2 ** N
    return result

# return not(x)
def negate(x):
    to_ret = ''
    for c in x:
        if(c == '1'):
            to_ret = to_ret + '0'
        else:
            to_ret = to_ret + '1'
    return to_ret

def twosComplement(x, N):
    return addSub('0' * N, x, '1', N, '0')

def binaryToHexStr(x):
    x = str(hex(int(x, 2)))
    if(x[-1] == 'L'):
        x = x[0:len(x) - 1]
    return x
    
# get flags
def get_N_flag():
    return mem.flagFile[0];
    
def set_N_flag():
    mem.flagFile[0] = '1';

def reset_N_flag():
    mem.flagFile[0] = '0';

def get_Z_flag():
    return mem.flagFile[1];
    
def set_Z_flag():
    mem.flagFile[1] = '1';
    
def reset_Z_flag():
    mem.flagFile[1] = '0';

def get_C_flag():
    return mem.flagFile[2];
    
def set_C_flag():
    mem.flagFile[2] = '1';
    
def reset_C_flag():
    mem.flagFile[2] = '0';

def get_V_flag():
    return mem.flagFile[3];
    
def set_V_flag():
    mem.flagFile[3] = '1';

def reset_V_flag():
    mem.flagFile[3] = '0';

def printAllFlags():
    print "flags(z,v,n,c): " + get_Z_flag() + "," + get_V_flag() + "," + get_N_flag() + "," + get_C_flag()
    
def printAllRegs():
    i = 0
    for x in mem.regFile:
        print str(i).zfill(2) + ": " + x
        i = i + 1

# usage give a binary of length <=N
# sign extends it and returns the resulting binary
def signExtend(binary, N):
    assert len(binary) <= N
    return binary[0] * (N - len(binary)) + binary

def zeroExtend(binary, N):
    assert len(binary) <= N
    return '0' * (N - len(binary)) + binary

def extend(x, N, unsigned):
    if(unsigned == 1):
       return zeroExtend(x, N)
    else:
       return signExtend(x, N)

def branchWithOffset(offset):  # signed offset
    armdebug.setPC((armdebug.getPC() + offset - 4))  # the magic! #-4 for the current instruction
    
def branchToAddress(hexint):  # give the exact address in int where to branch
    armdebug.setPC(hexint - 4)  # the magic again! #-4 for the current instruction
    
def PCwithOffset(offset):
    return armdebug.getPC()+offset#don't change this, it is no 4 only!!! 
    #why this? because the offset is always given from the current instruction
    
def PCwithPageOffset(N,offset):
    PCint=armdebug.getPC()
    PCbin=intToBinary(PCint, 64)
    PCbinModified=PCbin[0:52]+'0'*N
    PCnow=int(PCbinModified,2)
    return PCnow+offset
    
def conditionHolds(bits_four):
    # print 'condHolds'
    first_three = bits_four[0:3]
    # print first_three
    result = False
    cond = ''
    if first_three == '000':
        result = get_Z_flag() == '1'
        cond = 'EQ/NE'
        # print '1'
    elif first_three == '001':
        result = get_C_flag() == '1'
        cond = 'CS/CC'
        # print '2'
    elif first_three == '010':
        result = get_N_flag() == '1'
        cond = 'MI/PL'
        # print '3'
    elif first_three == '011':
        result = get_V_flag() == '1'
        cond = 'VS/VC'
        # print '4'
    elif first_three == '100':
        result = get_C_flag() == '1' and get_Z_flag() == '0'
        cond = 'HI/LS'
        # print '5'
    elif first_three == '101':
        result = (get_N_flag() == get_V_flag())
        cond = 'GE/LT'
        # print '6'
    elif first_three == '111':
        result = True
        cond = 'AL'
        # print'7'
        
    if bits_four[-1] == '1' and bits_four != '1111':
        result = not result
        # print '8'
    # print cond
    return (result, cond)

def getOffset(immkey):
    immkey=signExtend(immkey+'00', 64) #times 4 and 64 bits
    sign=immkey[0]
    offset=''
    inst=''
    if sign=='1':
        immkey=twosComplement(immkey, 64)
        inst+='-'
        offset=-int(immkey, 2)
    else:
        offset=int(immkey, 2)
    inst+=str(int(immkey, 2))
    return (inst, offset)

def getOffsetWithoutTimes(immkey):
    immkey=signExtend(immkey, 64) #no times 4 and 64 bits
    sign=immkey[0]
    offset=''
    inst=''
    if sign=='1':
        immkey=twosComplement(immkey, 64)
        inst+='-'
        offset=-int(immkey, 2)
    else:
        offset=int(immkey, 2)
    inst+=str(int(immkey, 2))
    return (inst, offset)

def decodeBitMasks(immN, imms, immr, M):
    len = highestSetBit(immN+negate(imms))
    levels = zeroExtend('1'*len, 6)
    s = uInt(logical_and(imms, levels))
    r = uInt(logical_and(immr, levels))
    diff = s-r
    esize = 1<<len
    d = uInt(intToBinary(diff, len))
    welem = zeroExtend('1'*(s+1), esize)
    telem = zeroExtend('1'*(d+1), esize)
    wmask = replicate(ror(welem, r), M)
    tmask = replicate(telem, M)
    return wmask,tmask

def replicate(x, N):
    while(len(x)<N):
        x = x+x
    return x
    
    
def highestSetBit(x):
    i = 0
    for c in x:
        if(c == '1'):
            return len(x)-i-1
        i = i+1
    return -1

#defining load and store methods over here
def loadFromMemory(hextr):
    #returns data from here
    pass


def storeToMemory(hexstr, data):
    #stores data here
    pass
