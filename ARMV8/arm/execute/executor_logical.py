'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils.utilFunc import *
from arm.test.temp import ror
from arm.utils import const
from arm.utils.mem import regFile
from elftools.construct.lib import hex

def execAnd_i32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAnd_i64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    setInstrFlag()
    
def execAnd_sr32(binary):    
    inst='AND '    
    rdKey=getRegKeyByStringKey(binary[27:32])
    rnKey=getRegKeyByStringKey(binary[22:27])
    rmKey=getRegKeyByStringKey(binary[11:16])    
    
    inst+=' W'+str(rdKey)+' W'+str(rnKey)+' W'+str(rmKey)+'{, '    
    
    rnValue = getRegValueByStringkey(binary[22:27])
    immvalue = int(binary[16:22],2) #amount
    rmValue = getRegValueByStringkey(binary[11:16])
    
    shifttype = binary[8:10]
    
    to_store=''
    temp=''
    
    if shifttype == "00":   
        temp=lsl(rmValue[32:64],immvalue)
        inst+=' LSL'
    elif shifttype == "01":
        temp=lsr(rmValue[32:64], immvalue)
        inst+=' LSR'
    elif shifttype == "10":
        temp=asr(rmValue[32:64], immvalue)
        inst+=' ASR'
    else:
        temp=ror(rmValue[32:64], immvalue)
        inst+=' ROR'
    inst+=' #'+str(immvalue)
    to_store=logical_and(temp, rnValue[32:64]).zfill(const.REG_SIZE)
    del regFile[rdKey]
    regFile.insert(rdKey,to_store)
    print inst
    setInstrFlag()
    
def execAnd_sr64(binary):    
    inst='AND '
    
    rdKey=getRegKeyByStringKey(binary[27:32])
    rnKey=getRegKeyByStringKey(binary[22:27])
    rmKey=getRegKeyByStringKey(binary[11:16])
    
    inst+=' W'+int(rdKey)+' W'+int(rnKey)+' W'+int(rmKey)+'{, '    
    
    rnValue = getRegValueByStringkey(binary[22:27])
    immvalue = int(binary[16:22],2) #amount
    rmValue = getRegValueByStringkey(binary[11:16])
    
    shifttype = binary[8:10]
    
    to_store=''
    temp=''
    
    if shifttype == "00":   
        temp=lsl(rmValue[0:64],immvalue)
        inst+=' LSL'
    elif shifttype == "01":
        temp=lsr(rmValue[0:64], immvalue)
        inst+=' LSR'
    elif shifttype == "10":
        temp=asr(rmValue[0:64], immvalue)
        inst+=' ASR'
    else:
        temp=ror(rmValue[0:64], immvalue)
        inst+=' ROR'
    inst+=' #'+immvalue
    to_store=logical_and(temp, rnValue[0:64]).zfill(const.REG_SIZE)
    print to_store  
    del regFile[rdKey]
    regFile.insert(rdKey,to_store)
    print inst
    setInstrFlag()
    


