'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils import dict, utilFunc

def decodeInstr(hexCode): 
    binary = utilFunc.hexToBin(hexCode)
    dict.MOVE_IMMEDIATE(binary)