'''
Created on Aug 8, 2014

@author: abhishek
'''

import utilFunc
from utilFunc import uInt, signExtend, getRegValueByStringkey

def execB(binary):
    inst ='B OFFSET('
    imm26key=binary[6:32]
    imm26key=utilFunc.signExtend(imm26key+'00', 64) #times 4 and 64 bits
    sign=imm26key[0]
    offset=''
    if sign=='1':
        imm26key=utilFunc.twosComplement(imm26key, 64)
        inst+='-'
        offset=-int(imm26key, 2)
    else:
        offset=int(imm26key, 2)
    inst+=str(int(imm26key, 2))
    inst= inst+')'
    utilFunc.branchWithOffset(offset) #the magic!
    utilFunc.finalize_simple(inst)
    
def execBCond(binary):
    bits_four=binary[-4:]
    #print 'bits four: '+bits_four
    xx=utilFunc.conditionHolds(bits_four)
    
    if not xx[0]:
        return
    #print xx[0]
    #print xx[1]
    inst ='B.'+xx[1]+' OFFSET('
    imm19key=binary[8:27]
    imm19key=utilFunc.signExtend(imm19key+'00', 64) #times 4 and 64 bits
    sign=imm19key[0]
    offset=''
    if sign=='1':
        imm19key=utilFunc.twosComplement(imm19key, 64)
        inst+='-'
        offset=-int(imm19key, 2)
    else:
        offset=int(imm19key, 2)
    inst+=str(int(imm19key, 2))
    inst=inst+')'
    utilFunc.branchWithOffset(offset) #the magic!
    utilFunc.finalize_simple(inst)
    
def execBL(binary):
    '''Not implemented yet'''
    
def execBR(binary):
    '''Not implemented yet'''
    
def execBLR(binary):
    '''Not implemented yet'''
    
def execRET(binary):
    '''Not implemented yet'''
    
def execCBZ_32(binary):
    CBZClass(binary, 32, True)
    
def execCBNZ_32(binary):
    CBZClass(binary, 32, False)
    '''Not implemented yet'''
    
def execCBZ_64(binary):
    CBZClass(binary, 64, True)
    
def execCBNZ_64(binary):
    CBZClass(binary, 64, False)
    '''Not implemented yet'''

'''def testB():
    binary=utilFunc.hexToBin('17fffffd')
    execB(binary)
    binary=utilFunc.hexToBin('14000002')
    execB(binary)    

def testBCond():
    utilFunc.set_N_flag()
    binary=utilFunc.hexToBin('54000024')
    execBCond(binary)
    
testBCond()'''
    
'''
utilFunc.set_Z_flag()
utilFunc.printAllFlags()
binary=utilFunc.hexToBin('5400002e')
execBCond(binary)'''

def CBZClass(binary,width,bool):
    rtKey=binary[-5:]
    inst='CBZ '
    char=''
    if width==64:
        char='X'
    else:
        char='W'
    inst+=char
    regnum=utilFunc.uInt(rtKey)
    inst+=str(regnum)+', OFFSET('
    imm19Key=binary[8:27]
    imm19Key=imm19Key+'00'
    imm19Key=utilFunc.signExtend(imm19Key, 64)
    sign=imm19Key[0]
    offset=''
    if sign=='1':
        imm19Key=utilFunc.twosComplement(imm19Key, 64)
        inst+='-'
        offset=-int(imm19Key, 2)
    else:
        offset=int(imm19Key, 2)
    inst+=str(int(imm19Key, 2))+')'
    regValue=getRegValueByStringkey(rtKey)
    regValue=regValue[0:width]#since CBZ_32
    if bool:
        if regValue=='0'*width:
            utilFunc.branchWithOffset(offset)
    else:
        if regValue!='0'*width:
            utilFunc.branchWithOffset(offset)
    utilFunc.finalize_simple(inst)
