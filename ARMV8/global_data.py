'''
Created on Aug 18, 2014

@author: abhiagar90
'''

import parsehelper
import mem

startAdd=''
numOfData=0
hexes=[]

def getHexes():
    global hexes
    return hexes

def setHexes(list_hex):
    global hexes
    hexes=list_hex

def setStartAddress(addr):
    global startAdd
    startAdd=addr
    
def getStartAddress():
    return startAdd
    
def getNumOfData():#!!! each data is 32 bit here
    return numOfData
    
def setNumOfData(num):
    global numOfData
    numOfData =  num
    
def getNumOfBytes():
    return getNumOfData()*4
    
def hasDataInData():
    global hexes
    return hexes==None or hexes==[]

def parseDataSection(filename):
    global hexes
    hexes=parsehelper.return_parsed_section(filename, '.data')
    if hexes:
        setStartAddress(parsehelper.getStartAddress())
        setNumOfData(parsehelper.getNumOfInst())
        #print hexes
        #print getStartAddress()
        saveAllToMemoryModel()
    
def checkIfValidDataAddress(givenHexString):
    startAdd=getStartAddress()
    length=getNumOfData()
    givenHexInt=int(givenHexString, 16)
    startAddInt=int(startAdd, 16)
    if (givenHexInt-startAddInt)%4 == 0:
        if(givenHexInt-startAddInt)/4 < length:
            return True
    return False

#call only when valid data address
def getDataIndexFromValidHexString(givenHexString): #starts at index 0
    startAdd=getStartAddress()
    givenHexInt=int(givenHexString, 16)
    startAddInt=int(startAdd, 16)
    return int((givenHexInt-startAddInt)/4)

#call only when valid data adddress
def loadDataFromData(givenHexString, wordlength):
    assert wordlength==1 or wordlength==2
    global hexes
    if checkIfValidDataAddress(givenHexString):
        num=getDataIndexFromValidHexString(givenHexString)
        if wordlength==1 :  return hexes[num]
        elif num+1<getNumOfData(): return hexes[num]+hexes[num+1]#just concatenating hexstrings will have to do conversion
    else:
        return 'trap'

def saveAllToMemoryModel():
    global hexes
    curAddrInt=int(getStartAddress(),16)
    for x in hexes:
        #x has the data
        mem.storeWordToMemory(hex(curAddrInt), x)
        curAddrInt+=4
    #mem.printMemoryState()