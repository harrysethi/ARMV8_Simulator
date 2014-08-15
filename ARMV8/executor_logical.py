'''
Created on Aug 8, 2014

@author: harinder
'''

from utilFunc import getRegKeyByStringKey, getRegValueByStringkey, lsl, lsr, asr, ror, logical_and, finalize

import const

def execAnd_i32(binary):
    '''Not implemented yet'''
    
def execAnd_i64(binary):
    '''Not implemented yet'''
    
    
def execAnd_sr32(binary):    
    inst='AND '
    rdKey=getRegKeyByStringKey(binary[27:32])
    rnKey=getRegKeyByStringKey(binary[22:27])
    rmKey=getRegKeyByStringKey(binary[11:16])    
    
    inst+='w'+str(rdKey)+', w'+str(rnKey)+', w'+str(rmKey)+', '    
    
    rnValue = getRegValueByStringkey(binary[22:27])
    immKey = binary[16:22]
    immvalue = int(immKey,2) #amount
    rmValue = getRegValueByStringkey(binary[11:16])
    
    shifttype = binary[8:10]
    
    temp=''
    
    if shifttype == "00":   
        temp=lsl(rmValue[32:64],immvalue)
        inst+='LSL'
    elif shifttype == "01":
        temp=lsr(rmValue[32:64], immvalue)
        inst+='LSR'
    elif shifttype == "10":
        temp=asr(rmValue[32:64], immvalue)
        inst+='ASR'
    else:
        temp=ror(rmValue[32:64], immvalue)
        inst+='ROR'
    inst+=' #'+str(immvalue)
    to_store=logical_and(temp, rnValue[32:64]).zfill(const.REG_SIZE)
    finalize(rdKey, to_store, inst)
    
def execAnd_sr64(binary):
    inst='AND '
    
    rdKey=getRegKeyByStringKey(binary[27:32])
    rnKey=getRegKeyByStringKey(binary[22:27])
    rmKey=getRegKeyByStringKey(binary[11:16])
    
    inst+='x'+str(rdKey)+', x'+str(rnKey)+', x'+str(rmKey)+', '
    
    rnValue = getRegValueByStringkey(binary[22:27])
    immKey = binary[16:22]
    immvalue = int(immKey,2) #amount
    rmValue = getRegValueByStringkey(binary[11:16])
    
    shifttype = binary[8:10]
    
    temp=''
    
    if shifttype == "00":   
        temp=lsl(rmValue[0:64],immvalue)
        inst+='LSL'
    elif shifttype == "01":
        temp=lsr(rmValue[0:64], immvalue)
        inst+='LSR'
    elif shifttype == "10":
        temp=asr(rmValue[0:64], immvalue)
        inst+='ASR'
    else:
        temp=ror(rmValue[0:64], immvalue)
        inst+='ROR'
    inst+=' #'+str(immvalue)
    to_store=logical_and(temp, rnValue[0:64]).zfill(const.REG_SIZE)
    finalize(rdKey, to_store, inst)
    