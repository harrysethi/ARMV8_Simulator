'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils import const

def hexToBin(s):
    scale = 16 ## equals to hexadecimal    
    binary = bin(int(s, scale))[2:].zfill(const.INST_SIZE)
    return binary
