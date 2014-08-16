'''
Created on Aug 8, 2014

@author: abhishek
'''

import utilFunc
from utilFunc import uInt, signExtend, getRegValueByStringkey
import armdebug

def execB(binary):
    inst ='B OFFSET('
    imm26key=binary[6:32]
    
    (instpart,offset)=getOffset(imm26key)
    inst+=instpart+')'
    
    utilFunc.branchWithOffset(offset) #the magic!
    utilFunc.finalize_simple(inst)
    
def execBCond(binary):
    
    bits_four=binary[-4:]
    xx=utilFunc.conditionHolds(bits_four)    
    if not xx[0]:
        return
    
    inst ='B.'+xx[1]+' OFFSET('
    imm19key=binary[8:27]
    
    (instpart,offset)=getOffset(imm19key)
    inst+=instpart+')'
    
    utilFunc.branchWithOffset(offset) #the magic!
    utilFunc.finalize_simple(inst)
    
def execBL(binary):
    inst='BL OFFSET('
    imm26key=binary[-26:]
    
    (instpart,offset)=getOffset(imm26key)
    inst+=instpart+')'
    
    nextAddr=armdebug.getPC()+4
    utilFunc.setRegValue(30, utilFunc.intToBinary(nextAddr, 64))
    utilFunc.branchWithOffset(offset)
    utilFunc.finalize_simple(inst)
    
def execBR(binary):
    inst = 'BR X'
    rnKey=binary[22:27]
    address_binary=utilFunc.getRegValueByStringkey(rnKey)
    regnum=utilFunc.uInt(rnKey)
    inst+=str(regnum)
    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        utilFunc.finalize_simple('Instruction aborted. Invalid instruction address in register.')
        return
    utilFunc.branchToAddress(int(hexstr,16))
    utilFunc.finalize_simple(inst)
    
def execBLR(binary):
    inst='BLR X'
    rnKey=binary[22:27]
    address_binary=utilFunc.getRegValueByStringkey(rnKey)
    regnum=utilFunc.uInt(rnKey)
    inst+=str(regnum)
    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        utilFunc.finalize_simple('Instruction aborted. Invalid instruction address in register.')
        return
    nextAddr=armdebug.getPC()+4
    utilFunc.setRegValue(30, utilFunc.intToBinary(nextAddr, 64))
    utilFunc.branchToAddress(int(hexstr,16))
    utilFunc.finalize_simple(inst)
    
def execRET(binary):
    inst = 'RET X'
    rnKey=binary[22:27]
    address_binary=utilFunc.getRegValueByStringkey(rnKey)
    regnum=utilFunc.uInt(rnKey)
    inst+=str(regnum)
    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        utilFunc.finalize_simple('Instruction aborted. Invalid instruction address in register.')
        return
    utilFunc.branchToAddress(int(hexstr,16))
    utilFunc.finalize_simple(inst)
    
def execCBZ_32(binary):
    CBZClass(binary, 32, True)
    
def execCBNZ_32(binary):
    CBZClass(binary, 32, False)
    
def execCBZ_64(binary):
    CBZClass(binary, 64, True)
    
def execCBNZ_64(binary):
    CBZClass(binary, 64, False)

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

    (instpart,offset)=getOffset(imm19Key)
    inst+=instpart+')'
    
    regValue=getRegValueByStringkey(rtKey)
    regValue=regValue[0:width]#since CBZ_32
    if bool:
        if regValue=='0'*width:
            utilFunc.branchWithOffset(offset)
    else:
        if regValue!='0'*width:
            utilFunc.branchWithOffset(offset)
    utilFunc.finalize_simple(inst)

def getOffset(immkey):
    immkey=utilFunc.signExtend(immkey+'00', 64) #times 4 and 64 bits
    sign=immkey[0]
    offset=''
    inst=''
    if sign=='1':
        immkey=utilFunc.twosComplement(immkey, 64)
        inst+='-'
        offset=-int(immkey, 2)
    else:
        offset=int(immkey, 2)
    inst+=str(int(immkey, 2))
    return (inst, offset)