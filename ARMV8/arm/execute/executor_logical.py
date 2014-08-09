'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils.utilFunc import *
from arm.test.temp import ror
from arm.utils import const
from arm.utils.mem import regFile

def execAnd_i32(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    
def execAnd_i64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)
    
def execAnd_sr32(binary):    
    rdKey=getRegKeyByStringKey(binary[27:32])
    rnValue = getRegValueByStringkey(binary[22:27])
    immvalue = int(binary[16:22],2) #amount
    rmValue = getRegValueByStringkey(binary[11:16])
    shifttype = binary[8:10]
    
    to_store=''
    temp=''
    
    if shifttype == "00":   
        temp=lsl(rmValue[32:64],immvalue)
    elif shifttype == "01":
        temp=lsr(rmValue[32:64], immvalue)
    elif shifttype == "10":
        temp=asr(rmValue[32:64], immvalue)
    else:
        temp=ror(rmValue, immvalue)
    to_store=logical_and(temp, rnValue).zfill(const.REG_SIZE)
    print to_store    
    del regFile[rdKey]
    regFile.insert(rdKey,to_store)
    
    
def execAnd_sr64(binary):
    rdKey = int(binary[27:32],2)
    rnKey = int(binary[22:27],2)



