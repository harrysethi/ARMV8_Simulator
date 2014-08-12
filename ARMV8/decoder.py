'''
Created on Aug 8, 2014

@author: harinder
'''

import dicts
import utilFunc
import const

def decodeInstr(hexCode): 
    binary = utilFunc.hexToBin(hexCode)
    for i in range(7):        
        dicts.INSTRUCTION_TYPE(binary, i)
        if(const.FLAG_INST_EXECUTED=="1"):
            break
