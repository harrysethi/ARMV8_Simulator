'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils import dict, utilFunc
from arm.utils import const

def decodeInstr(hexCode): 
    binary = utilFunc.hexToBin(hexCode)
    for i in range(7):        
        dict.INSTRUCTION_TYPE(binary, i)
        if(const.FLAG_INST_EXECUTED=="1"):
            break
