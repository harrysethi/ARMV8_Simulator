'''
Created on Aug 8, 2014

@author: abhishek
'''
import const
import utilFunc
import armdebug


def execB(binary):
    inst ='B OFFSET('
    imm26key=binary[6:32]
    #print imm26key
    imm26key=utilFunc.signExtend(imm26key+'00', 64) #times 4 and 64 bits
    #print imm26key
    sign=imm26key[0]
    offset=''
    if sign=='1':
        imm26key=utilFunc.twosComplement(imm26key, 64)
        inst+='-'
        offset=0-int(imm26key, 2)
    inst+=str(int(imm26key, 2))
    offset=int(imm26key, 2)
    print inst+')'
    armdebug.setPC(armdebug.getPC()+offset) #the magic!
    
def execBCond(binary):
    inst ='B OFFSET('
    imm26key=binary[6:32]
    #print imm26key
    imm26key=utilFunc.signExtend(imm26key+'00', 64) #times 4 and 64 bits
    #print imm26key
    sign=imm26key[0]
    offset=''
    if sign=='1':
        imm26key=utilFunc.twosComplement(imm26key, 64)
        inst+='-'
        offset=0-int(imm26key, 2)
    inst+=str(int(imm26key, 2))
    offset=int(imm26key, 2)
    print inst+')'
    armdebug.setPC(armdebug.getPC()+offset) #the magic!

'''def testB():
    binary=utilFunc.hexToBin('17fffffd')
    execB(binary)
    binary=utilFunc.hexToBin('14000002')
    execB(binary)
    
    
testB()'''
    
def execBL(binary):
    '''Not implemented yet'''
    
def execBR(binary):
    '''Not implemented yet'''
    
def execBLR(binary):
    '''Not implemented yet'''
    
def execRET(binary):
    '''Not implemented yet'''
    
def execCBZ_32(binary):
    '''Not implemented yet'''
    
def execCBNZ_32(binary):
    '''Not implemented yet'''
    
def execCBZ_64(binary):
    '''Not implemented yet'''
    
def execCBNZ_64(binary):
    '''Not implemented yet'''
