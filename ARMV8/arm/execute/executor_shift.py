'''
Created on Aug 8, 2014

@author: harinder
'''

from arm.utils.utilFunc import setInstrFlag
from arm.utils.mem import regFile
from arm.utils import utilFunc
from arm.utils.utilFunc import finalize

#Helper function
def getFields_r(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    rnVal = regFile[rnKey]
    rmVal = regFile[rmKey]
    return rdKey, rnKey, rmKey, rnVal, rmVal


def execAsr_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'ASR w'+str(rdKey)+", w"+str(rnKey)+", w"+str(rmKey)
    rd = '0'*32+utilFunc.asr(rnVal[32:64], int(rmVal[59:64],2))
    finalize(rdKey, rd, instr)
                       
def execLsl_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'LSL w'+str(rdKey)+", w"+str(rnKey)+", w"+str(rmKey)
    rd = '0'*32+utilFunc.lsl(rnVal[32:64], int(rmVal[59:64],2))
    finalize(rdKey, rd, instr)
    
def execLsr_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'LSR w'+str(rdKey)+", w"+str(rnKey)+", w"+str(rmKey)
    rd = '0'*32+utilFunc.lsr(rnVal[32:64], int(rmVal[59:64],2))
    finalize(rdKey, rd, instr)
    
def execAsr_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'ASR x'+str(rdKey)+", x"+str(rnKey)+", x"+str(rmKey)
    rd = utilFunc.asr(rnVal, int(rmVal[58:64],2))
    finalize(rdKey, rd, instr)
                       
def execLsl_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'LSL x'+str(rdKey)+", x"+str(rnKey)+", x"+str(rmKey)
    rd = utilFunc.lsl(rnVal, int(rmVal[58:64],2))
    finalize(rdKey, rd, instr)
    
def execLsr_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'LSR x'+str(rdKey)+", x"+str(rnKey)+", x"+str(rmKey)
    rd = utilFunc.lsr(rnVal, int(rmVal[58:64],2))
    finalize(rdKey, rd, instr)

