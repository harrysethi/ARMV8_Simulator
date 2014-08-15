'''
Created on Aug 8, 2014

@author: abhishek
'''

import utilFunc

def conditionHolds(bits_four):
    first_three=bits_four[0:3]
    result=False
    cond=''
    if first_three=='000':
        result=utilFunc.get_Z_flag()=='1'
        cond='EQ/NE'
    elif first_three=='001':
        result=utilFunc.get_C_flag()=='1'
        cond='CS/CC'
    elif first_three=='010':
        result=utilFunc.get_N_flag()=='1'
        cond='MI/PL'
    elif first_three=='011':
        result=utilFunc.get_V_flag()=='1'
        cond='VS/VC'
    elif first_three=='100':
        result=utilFunc.get_C_flag()=='1' and utilFunc.get_Z_flag()=='0'
        cond='HI/LS'
    elif first_three=='101':
        result=utilFunc.get_N_flag()==utilFunc.get_V_flag()
        cond='GE/LT'
    elif first_three=='111':
        result=True
        cond='AL'
        
    if bits_four[3]=='1' and bits_four!='1111':
        result= not result
        
    return result, cond

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
    print inst+')'
    utilFunc.branchWithOffset(offset) #the magic!
    
def execBCond(binary):
    bits_four=binary[-4]
    result, cond=conditionHolds(bits_four)
    if not result:
        return
    
    inst ='B.'+cond+' OFFSET('
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
    print inst+')'
    utilFunc.branchWithOffset(offset) #the magic!
    

    
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

def testB():
    binary=utilFunc.hexToBin('17fffffd')
    execB(binary)
    binary=utilFunc.hexToBin('14000002')
    execB(binary)    

def testBCond():
    binary=utilFunc.hexToBin('5400002e')
    execBCond(binary)
    
testBCond()