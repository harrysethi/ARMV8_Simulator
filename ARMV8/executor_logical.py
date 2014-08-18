'''
Created on Aug 8, 2014

@author: harinder
'''

import utilFunc

import const

def op_i(binary, N):
    inst = 'AND '
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rnValue = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    if(N == 32):
        r = 'w'
        rnValue = rnValue[32:64]
    else:
        r = 'x'
    inst += r + str(rdKey) + ', ' + r + str(rnKey)
    
    
    immr = binary[10:16]
    imms = binary[16:22]
    immN = binary[9]
    
    imm, temp = utilFunc.decodeBitMasks(immN, imms, immr, N)
    inst += ', #' + str(int(imm,2))
    result = utilFunc.logical_and(rnValue,imm).zfill(const.REG_SIZE)
    utilFunc.finalize(rdKey, result, inst, '1')

def execAnd_i32(binary):
    op_i(binary, 32)
    
    
def execAnd_i64(binary):
    op_i(binary, 64)
    
    
def execAnd_sr32(binary):    
    inst = 'AND '
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])    
    
    inst += 'w' + str(rdKey) + ', w' + str(rnKey) + ', w' + str(rmKey) + ', '    
    
    rnValue = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    immKey = binary[16:22]
    immvalue = int(immKey, 2)  # amount
    rmValue = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    
    shifttype = binary[8:10]
    
    temp = ''
    
    if shifttype == "00":   
        temp = utilFunc.lsl(rmValue[32:64], immvalue)
        inst += 'LSL'
    elif shifttype == "01":
        temp = utilFunc.lsr(rmValue[32:64], immvalue)
        inst += 'LSR'
    elif shifttype == "10":
        temp = utilFunc.asr(rmValue[32:64], immvalue)
        inst += 'ASR'
    else:
        temp = utilFunc.ror(rmValue[32:64], immvalue)
        inst += 'ROR'
    inst += ' #' + str(immvalue)
    to_store = utilFunc.logical_and(temp, rnValue[32:64]).zfill(const.REG_SIZE)
    utilFunc.finalize(rdKey, to_store, inst, '0')
    
def execAnd_sr64(binary):
    inst = 'AND '
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    
    inst += 'x' + str(rdKey) + ', x' + str(rnKey) + ', x' + str(rmKey) + ', '
    
    rnValue = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    immKey = binary[16:22]
    immvalue = int(immKey, 2)  # amount
    rmValue = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    
    shifttype = binary[8:10]
    
    temp = ''
    
    if shifttype == "00":   
        temp = utilFunc.lsl(rmValue[0:64], immvalue)
        inst += 'LSL'
    elif shifttype == "01":
        temp = utilFunc.lsr(rmValue[0:64], immvalue)
        inst += 'LSR'
    elif shifttype == "10":
        temp = utilFunc.asr(rmValue[0:64], immvalue)
        inst += 'ASR'
    else:
        temp = utilFunc.ror(rmValue[0:64], immvalue)
        inst += 'ROR'
    inst += ' #' + str(immvalue)
    to_store = utilFunc.logical_and(temp, rnValue[0:64]).zfill(const.REG_SIZE)
    utilFunc.finalize(rdKey, to_store, inst, '0')
    
