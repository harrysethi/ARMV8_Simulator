'''
Created on Aug 8, 2014

@author: harinder
'''

import dicts
import utilFunc
import const

def decodeInstr(hexCode): 
    binary = utilFunc.hexToBin(hexCode)
    
    #Checking for branch type
    if(binary[3:6] == '101'):
        for i in range(3):
            dicts_branch.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_INST_EXECUTED=="1"):
                break
    
    #Checking for load-store
    elif(binary[4] == '1' and binary[6] == '0'):
        for i in range(7):
            dicts_loadStore.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_INST_EXECUTED=="1"):
                break
    
    else:        
        for i in range(7):        
            dicts.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_INST_EXECUTED=="1"):
                break
