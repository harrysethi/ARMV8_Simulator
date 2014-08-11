'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils import const
from arm.utils.mem import regFile
from arm.utils import utilFunc


def execMov_iwi32(binary):
    instr = "MOV w" + mov_imm(binary)
    print instr
    
def execMov_iwi64(binary):
    instr = "MOV x" + mov_imm(binary)
    print instr
    
def execMov_wi32(binary):
    instr = "MOV w" + mov_imm(binary)
    print instr
    
def execMov_wi64(binary):    
    instr = "MOV x" + mov_imm(binary)
    print instr
    
def mov_imm(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    instr = str(rdKey)+", "+hex(int(imm16,2))
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
    utilFunc.setInstrFlag()
    return instr
                       
def execMov_bmi32(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    
def execMov_bmi64(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
