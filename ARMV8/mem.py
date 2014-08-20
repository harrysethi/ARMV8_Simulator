'''
Created on Aug 8, 2014

@author: harinder
'''
import parsehelper, const

regNum=32
#31st register is used for SP
regFile = list('0'*64 for i in range(regNum))

#flags-order: n,z,c,v
flagFile = list('0' for i in range(4))

memory_model={}

helper_memory_model={}

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


#will have to use int for address!!!
#data is 4 bytes here in a 8 hexit string like 09090909

def storeWordToMemory(address, data):
    #print 'being called here'
    global memory_model
    memory_model[address]=data
    storeWordToHelperMemory(address, data)
    
def storeWordToHelperMemory(address,data):
    global helper_memory_model
    #data is 8 hexit : 01020304
    #spilt first
    list=[data[0:2],data[2:4],data[4:6],data[6:8]]
    if parsehelper.isLittle():
        list.reverse()
    #print list
    #now each data is 2 hexit
    helper_memory_model[address]=list[0]
    helper_memory_model[address+1]=list[1]
    helper_memory_model[address+2]=list[2]
    helper_memory_model[address+3]=list[3]
    
def fetchByteFromHelperMemory(address):
    global helper_memory_model
    try:
        return helper_memory_model[address]
    except KeyError:
        return const.TRAP
    
#give an int equivalent of address
#will fetch only a word
def fetchWordFromMemory(address):
    global memory_model
    try:
        return memory_model[address]
    except KeyError:
        return const.TRAP
    
def printMemoryState():
    global memory_model
    print memory_model
    printHelperMemoryState()
    
def printHelperMemoryState():
    global helper_memory_model
    print helper_memory_model
    
def init():
    global regFile, flagFile, memory_model, regNum, watchReg
    regNum=31

    regFile = list('0'*64 for i in range(regNum))
    #flags-order: n,z,c,v
    flagFile = list('0' for i in range(4))

    memory_model={}

    watchReg = list(False for i in range(regNum))