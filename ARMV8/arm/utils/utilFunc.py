'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils import const

def hexToBin(s):
    scale = 16 ## equals to hexadecimal    
    binary = bin(int(s, scale))[2:].zfill(const.INST_SIZE)
    return binary

def lsl(s,i):
    s=s[i:len(s)]+'0'*i
    
def lsr(s,i):
    s='0'*i+s[0:len(s)-i]
    
def asr(s,i):
    s=s[0]*i+s[0:len(s)-i]
    

        
