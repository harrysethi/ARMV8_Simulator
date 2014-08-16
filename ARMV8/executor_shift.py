'''
@author: harinder
'''


import utilFunc
import mem


# Helper function
def getFields_r(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27])
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16])
    return rdKey, rnKey, rmKey, rnVal, rmVal


def execAsr_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'ASR w' + str(rdKey) + ", w" + str(rnKey) + ", w" + str(rmKey)
    rd = '0' * 32 + utilFunc.asr(rnVal[32:64], int(rmVal[59:64], 2))
    utilFunc.finalize(rdKey, rd, instr)
                       
def execLsl_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'LSL w' + str(rdKey) + ", w" + str(rnKey) + ", w" + str(rmKey)
    rd = '0' * 32 + utilFunc.lsl(rnVal[32:64], int(rmVal[59:64], 2))
    utilFunc.finalize(rdKey, rd, instr)
    
def execLsr_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'LSR w' + str(rdKey) + ", w" + str(rnKey) + ", w" + str(rmKey)
    rd = '0' * 32 + utilFunc.lsr(rnVal[32:64], int(rmVal[59:64], 2))
    utilFunc.finalize(rdKey, rd, instr)
    
def execAsr_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'ASR x' + str(rdKey) + ", x" + str(rnKey) + ", x" + str(rmKey)
    rd = utilFunc.asr(rnVal, int(rmVal[58:64], 2))
    utilFunc.finalize(rdKey, rd, instr)
                       
def execLsl_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'LSL x' + str(rdKey) + ", x" + str(rnKey) + ", x" + str(rmKey)
    rd = utilFunc.lsl(rnVal, int(rmVal[58:64], 2))
    utilFunc.finalize(rdKey, rd, instr)
    
def execLsr_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    instr = 'LSR x' + str(rdKey) + ", x" + str(rnKey) + ", x" + str(rmKey)
    rd = utilFunc.lsr(rnVal, int(rmVal[58:64], 2))
    utilFunc.finalize(rdKey, rd, instr)

# Immediate operations
def execAsr_i32(binary):    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(imms == '011111'):
        shiftVal = int(immr,2)
        instr = 'ASR w' + str(rdKey) + ", w" + str(rnKey) + ", #" + str(shiftVal)
        rd = '0' * 32 + utilFunc.asr(rnVal[32:64], shiftVal)
        utilFunc.finalize(rdKey, rd, instr)
    
def execAsr_i64(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(imms == '111111'):
        shiftVal = int(immr,2)
        instr = 'ASR x' + str(rdKey) + ", x" + str(rnKey) + ", #" + str(shiftVal)
        rd = utilFunc.asr(rnVal, shiftVal)
        utilFunc.finalize(rdKey, rd, instr)
                       
def execLslLsr_i32(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    immrVal = int(immr,2)
    immsVal = int(imms,2)
    if(imms == '011111'):
        #LSR
        shiftVal = immrVal
        instr = 'LSR w' + str(rdKey) + ", w" + str(rnKey) + ", #" + str(shiftVal)
        rd = '0' * 32 + utilFunc.lsr(rnVal[32:64], shiftVal)
    elif(immrVal == immsVal+1):
        #LSL
        shiftVal = 63-immsVal
        instr = 'LSL w' + str(rdKey) + ", w" + str(rnKey) + ", #" + str(shiftVal)
        rd = '0' * 32 + utilFunc.lsl(rnVal[32:64], shiftVal)
    utilFunc.finalize(rdKey, rd, instr)
    
def execLslLsr_i64(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    immrVal = int(immr,2)
    immsVal = int(imms,2)
    if(imms == '111111'):
        #LSR
        shiftVal = immrVal
        instr = 'LSR x' + str(rdKey) + ", x" + str(rnKey) + ", #" + str(shiftVal)
        rd = utilFunc.lsr(rnVal, shiftVal)
    elif(immrVal == immsVal+1):
        #LSL
        shiftVal = 63-immsVal
        instr = 'LSL x' + str(rdKey) + ", x" + str(rnKey) + ", #" + str(shiftVal)
        rd = utilFunc.lsl(rnVal, shiftVal)
    utilFunc.finalize(rdKey, rd, instr)
    

# Helper function
def getFields_i(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    immr = binary[10:16]
    imms = binary[16:22]
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27])
    return rdKey, rnKey, rnVal, immr, imms
