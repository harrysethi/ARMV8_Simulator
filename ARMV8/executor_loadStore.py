'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc


def execMov_iwi32(binary):
    mov_imm(binary, "MOV w", '1', 32)
    
def execMov_iwi64(binary):
    mov_imm(binary, "MOV x", '1', 64)
    
def execMov_wi32(binary):
    mov_imm(binary, "MOV w", '0', 32)
    
def execMov_wi64(binary):
    mov_imm(binary, "MOV x", '0', 64)
    
def mov_imm(binary, instr, inverted, N):    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    hw = binary[9:11]
    pos = utilFunc.uInt(hw+'0000')
    
    imm16 = binary[11:27]
    result = (imm16+'0'*pos).zfill(N)
    if(inverted == '1'):
        result = utilFunc.negate(result)
    instr = instr + str(rdKey)+", #"+utilFunc.binaryToHexStr(result)
    utilFunc.finalize(rdKey, result.zfill(const.REG_SIZE), instr)
                       
def execMov_bmi32(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    
def execMov_bmi64(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
