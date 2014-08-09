'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils import const
from arm.utils.mem import regFile
from arm.utils.utilFunc import *


def execMov_iwi32(binary):
    rdKey = getRegKeyByStringKey(binary[27:32])
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    print "MOV w"+str(rdKey)+", "+hex(int(imm16,2))
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
    
def execMov_iwi64(binary):
    rdKey = getRegKeyByStringKey(binary[27:32])
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    print "MOV x"+str(rdKey)+", "+hex(int(imm16,2))
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
    
def execMov_wi32(binary):
    rdKey = getRegKeyByStringKey(binary[27:32])
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    print "MOV w"+str(rdKey)+", "+hex(int(imm16,2))
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
    
def execMov_wi64(binary):
    rdKey = getRegKeyByStringKey(binary[27:32])
    imm16 = binary[11:27].zfill(const.REG_SIZE)
    print "MOV x"+str(rdKey)+", "+hex(int(imm16,2))
    del regFile[rdKey]
    regFile.insert(rdKey,imm16)
                       
def execMov_bmi32(binary):
    rdKey = getRegKeyByStringKey(binary[27:32])
    
def execMov_bmi64(binary):
    rdKey = getRegKeyByStringKey(binary[27:32])
