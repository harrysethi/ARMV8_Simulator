'''
Created on Aug 8, 2014

@author: harinder
'''

regNum=32
#31st register is used for SP
regFile = list('0'*64 for i in range(regNum))

#flags-order: n,z,c,v
flagFile = list('0' for i in range(4))

memory_model={}

watchReg = list(False for i in range(regNum))


def setWatchForReg(index):
    global watchReg
    del watchReg[index]
    watchReg.insert(index, True)
    
def resetWatchForReg(index):
    global watchReg
    del watchReg[index]
    watchReg.insert(index, False)
    
def printWatchStateAll():
    global watchReg
    
#regKey should be the correct index of the register 0 to 31
#watch on stack pointer too?
def isWatchSet(regKey):
    global watchReg
    return watchReg[regKey]
    pass

def setGlobalDataMemory(startAddress, list):
    pass

#both are hex strings! wrong!
#will have to use int for address!!!
#assume data is 4 bytes here
def storeWordToMemory(address, data):
    #print 'being called here'
    global memory_model
    memory_model[address]=data
    
#give an int equivalent of address
#will fetch only a word
def fetchWordFromMemory(address):
    global memory_model
    try:
        return memory_model[address]
    except KeyError:
        return 'trap'
    
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
    
