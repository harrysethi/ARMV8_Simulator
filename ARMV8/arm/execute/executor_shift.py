'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils.utilFunc import setInstrFlag
from arm.utils.mem import regFile
from arm.utils import const


def execAsr_r32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    rmkey = int(binary[11:16],2)
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
    setInstrFlag()
                       
def execLsl_r32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execLsr_r32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAsr_r64(binary):
    rdKey = int(binary[27:32],2)
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
    setInstrFlag()
                       
def execLsl_r64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execLsr_r64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()