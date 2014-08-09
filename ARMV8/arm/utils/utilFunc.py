'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.utils import const
from arm.utils.mem import regFile

def hexToBin(s):
    scale = 16 ## equals to hexadecimal    
    binary = bin(int(s, scale))[2:].zfill(const.INST_SIZE)
    return binary

def lsl(s,i):
    return s[i:len(s)]+'0'*i
    
def lsr(s,i):
   return '0'*i+s[0:len(s)-i]
    
def asr(s,i):
    return s[0]*i+s[0:len(s)-i]
    
def ror(s,i):
    for x in range(i):
        s=s[-1]+s[0:len(s)-1]
    return s

#gives 64 bit, truncate when using
#key should be broen already        
def getRegValueByStringkey(key):  
    key = int(key,2)
    return regFile[key]

def getRegKeyByStringKey(key):
    key = int(key,2)
    return key

#assuming both s1 and s2 have same length    
def logical_and(s1,s2):
    to_return=''
    if len(s1)!=len(s2):
        print 'Implementation error. Lengths not equal'
        exit(1)
    else:        
        for x in range(len(s1)):
            if s1[x]!=s2[x]:
                to_return+='0'
            elif s1[x] == '0':
                to_return+='0'
            else:
                to_return+='1'
    return to_return