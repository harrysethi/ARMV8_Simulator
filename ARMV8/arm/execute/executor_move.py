'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils import const
from arm.utils.mem import regFile

def execMov_i(binary):
    rdKey = int(binary[27:32],2)
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
                       
def execMov_bmi32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    
def execMov_bmi64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)