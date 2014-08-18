'''
Created on Aug 8, 2014

@author: harinder
'''

regNum=31

regFile = list('0'*64 for i in range(32))
#flags-order: n,z,c,v
flagFile = list('0' for i in range(4))

memory_model={}

watchReg = list(False for i in range(regNum))


def setWatchForReg(index):
    del watchReg[index]
    watchReg[index]=True
    
def resetWatchForReg(index):
    del watchReg[index]
    watchReg[index]=False
    
def printWatchStateAll():
    print watchReg
    
#regKey should be the correct index of the register 0 to 31
#watch on stack pointer too?
def isWatchSet(regKey):
    return watchReg[regKey]
    pass

def setGlobalDataMemory(startAddress, list):
    pass

#both are hex strings 
#assume data is 4 bytes here
def storeWordToMemory(address, data):
    global memory_model
    memory_model[address]=data
    
def printMemoryState():
    print memory_model
    
