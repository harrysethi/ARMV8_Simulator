'''
Created on Aug 8, 2014

@author: harinder
'''


regFile = list('0'*64 for i in range(31))
#flags-order: n,z,c,v
flagFile = list('0' for i in range(4))

memory_model={}

def setGlobalDataMemory(startAddress, list):
    pass

#both are hex strings 
#assume data is 4 bytes here
def storeWordToMemory(address, data):
    global memory_model
    memory_model[address]=data
    
def printMemoryState():
    print memory_model