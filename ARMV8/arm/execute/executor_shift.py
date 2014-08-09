'''
Created on Aug 8, 2014

@author: harinder
'''
def execAsr_r32(binary):
    rdKey = int(binary[27:32],2)
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
                       
def execLsl_r32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    
def execLsr_r32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    
def execAsr_r64(binary):
    rdKey = int(binary[27:32],2)
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
                       
def execLsl_r64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    
def execLsr_r64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)