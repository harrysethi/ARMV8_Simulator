'''
Created on Aug 8, 2014

@author: harinder
'''

regNum=31

regFile = list('0'*64 for i in range(regNum))
#flags-order: n,z,c,v
flagFile = list('0' for i in range(4))

memory_model={}

watchReg = list(False for i in range(regNum))


def setWatchForReg(index):
    global watchReg
    #print 'before: '+str(len(watchReg))
    del watchReg[index]
    watchReg.insert(index, True)
    #print 'after: '+str(len(watchReg))
    
def resetWatchForReg(index):
    global watchReg
    del watchReg[index]
    watchReg.insert(index, False)
    #print len(watchReg)
    
def printWatchStateAll():
    global watchReg
    #print watchReg
    
#regKey should be the correct index of the register 0 to 31
#watch on stack pointer too?
def isWatchSet(regKey):
    global watchReg
    #print 'len here: '+str(len(watchReg))
    return watchReg[regKey]
    pass

def setGlobalDataMemory(startAddress, list):
    pass

#both are hex strings 
#assume data is 4 bytes here
def storeWordToMemory(address, data):
    #print 'being called here'
    global memory_model
    memory_model[address]=data
    
def printMemoryState():
    print memory_model
    
def init():
    global regFile, flagFile, memory_model, regNum, watchReg
    regNum=31

    regFile = list('0'*64 for i in range(regNum))
    #flags-order: n,z,c,v
    flagFile = list('0' for i in range(4))

    memory_model={}

    watchReg = list(False for i in range(regNum))
    
