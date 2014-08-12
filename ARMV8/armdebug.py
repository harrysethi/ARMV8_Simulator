'''
Created on 11-Aug-2014

@author: abhiagar90@gmail.com
'''

import re
import parsehelper
import utilFunc
import decoder
import mem
from utilFunc import binaryToHexStr

DEBUG_MODE=False
PC = 0
bkpoint=[]
hexes=[]

def getHexes():
    global hexes
    return hexes

def setHexes(list_hex):
    global hexes
    hexes=list_hex
    
def startDebugMode():
    global DEBUG_MODE
    DEBUG_MODE=True
    
def endDebugMode():
    global DEBUG_MODE
    DEBUG_MODE=False
    
def isDebugMode():
    global DEBUG_MODE
    return DEBUG_MODE  
 
def checkIfValidBreakPoint(givenHexString):
    length=parsehelper.getNumOfInst()
    givenHexInt=int(givenHexString, 16)
    prog_counter=getPC()
    if (givenHexInt-prog_counter)%4 == 0:
        if (givenHexInt-prog_counter)/4 < length and int((givenHexInt-prog_counter)/4) >= getCurrentInstNumber():
            return True
    return False

def checkIfValidBreakPoint2(givenHexString):
    startAdd=parsehelper.getStartAddress()
    length=parsehelper.getNumOfInst()
    givenHexInt=int(givenHexString, 16)
    startAddInt=int(startAdd, 16)
    if (givenHexInt-startAddInt)%4 == 0:
        if(givenHexInt-startAddInt)/4 < length:
            return True
    return False

#Note could be 5 etc, any int
def setPC(givenInt):
    global PC
    PC = givenInt
    
def getPC():
    global PC
    return PC

def incPC():
    global PC
    PC=PC+4

def getCurrentInstNumber(): #starts at index 0
    prog_counter=getPC()
    start=int(parsehelper.getStartAddress(),16)
    return int((prog_counter-start)/4)

def getInstFromValidHexString(givenHexString): #starts at index 0
    startAdd=parsehelper.getStartAddress()
    givenHexInt=int(givenHexString, 16)
    startAddInt=int(startAdd, 16)
    return int((givenHexInt-startAddInt)/4)
    pass
   

def initBkPoint():
    global bkpoint
    length=parsehelper.getNumOfInst()
    bkpoint= [False for x in range(length)]
    #print bkpoint
    
def putBkPoint(givenHexString):
    num=-1
    if checkIfValidBreakPoint(givenHexString):
        num=getInstFromValidHexString(givenHexString)
    if num != -1:
        #list nuances
        del bkpoint[num]
        bkpoint.insert(num, True)
        return True
    else:
        return False
    
def resetBkPoint(givenHexString):
    num=-1
    if checkIfValidBreakPoint(givenHexString):
        num=getInstFromValidHexString(givenHexString)
    if num != -1:
        #list nuances
        del bkpoint[num]
        bkpoint.insert(num, False)
        return True
    else:
        return False
    
def isBkPoint(index):
    if(index < len(getHexes())):
        global bkpoint
        return bkpoint[index]

def isBkPointHex(givenHexString): #assume the hex is within limits and right always
    index=getInstFromValidHexString(givenHexString)
    return isBkPoint(index)
    
def startInteraction():
    flag = True
    initBkPoint()
    setPC(int(parsehelper.getStartAddress(),16))
    #print getPC()
    #print getCurrentInstNumber()
    print '------------------------------------'
    print 'The starting address is: ' + parsehelper.getStartAddress()
    print "Debug mode started. Type 'help' for list of options."
    while flag:
        print '------------------------------------'
        print 'Type debug commnand here : ',
        x=raw_input()
        x=x.strip().lower()
        if x=='exit':
            flag=False
        else:
            parseCommand(x)

def parseCommand(command):
    if command=='' or command==None:
        return
    
    print 'Typed: '+command
    
    if command=='s':
        executeS()
        return
    
    if command=='run':
        executeRUN()
        return 
    
    if command=='c':
        executeC()
        return
    
    if command.startswith('break'):
        executeBreak(command.split()[1])
        return
    
    if command.startswith('del'):
        executeDel(command.split()[1])
        return
    
    if command.startswith('print'):
        executePrint(command)
        return
    
    if command == 'flags':
        executeFlag()
        return
    
    if command == 'regs':
        executeRegs()
        return
    
    if command == 'help':
        executeDebuggerHelp()
        return
    
    else:
        print 'Not supported input (yet)!'
    
def executeS():
    #will have to take care of inst running also
    #not caring about break point or not -->DOESN't MATTER
    print "Executing command type: "+"'s'"
    executeNextInst()
    pass

def executeNextInst():
    if getCurrentInstNumber()<len(getHexes()):
        hexcode=hexes[getCurrentInstNumber()]
        utilFunc.resetInstrFlag()
        decoder.decodeInstr(hexcode)
        incPC()
    else:
        print 'instructions exhausted!!'
    #print 'PC: '+str(getPC())

def executeRUN():
    print "Executing command type: "+"'run'"
    x=getCurrentInstNumber()
    if(x>=len(getHexes())):
        print 'instructions exhausted!!'
        return
    while (x <  len(getHexes())):
        #print 'X: '+str(x)
        executeNextInst()
        x=getCurrentInstNumber()
        
def executeBreak(address): 
    #print 'You typed address: '+address
    #assuming should start with address
    if len(address)!=10:
        print 'Not valid hex address for current state'
        return
    myhex=re.findall(r'0[x|X][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]', address)
    print myhex
    if myhex:
        #print mylist[0]
        if(checkIfValidBreakPoint(myhex[0])):
            if not isBkPointHex(myhex[0]):
                putBkPoint(myhex[0])
                print 'break done...'
            else:
                print 'already a breakpoint'
        else:
            print 'Not valid hex address for current state'
    else:
        print 'Not valid hex address for current state'
        return
    
def executeDel(address): 
    #print 'You typed address: '+address
    #assuming should start with address
    
    if len(address)!=10:
        print 'Not valid hex address for current state'
        return
    
    myhex=re.findall(r'0[x|X][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]', address)
    print myhex
    if myhex:
        #print mylist[0]
        if(checkIfValidBreakPoint(myhex[0])):
            if isBkPointHex(myhex[0]):
                resetBkPoint(myhex[0])
                print 'del done...'
            else:
                print 'already not a breakpoint'
        else:
            print 'Not valid hex address for current state'
    else:
        print 'Not valid hex address for current state'
        
    
def executeC():
    print "Executing command type: "+"'c'"
    x=getCurrentInstNumber()
    if(x >= len(getHexes())):
        print 'instructions exhausted!!'
        return
    while (x <  len(getHexes()) and (not isBkPoint(x))):
        #print 'X: '+str(x)
        executeNextInst()
        x=getCurrentInstNumber()
        print 'no breakpoints encountered. instructions exhausted!!'
    if (x==len(getHexes())):
        return 
    print "Arrived at the break point. Type 's' or 'run'..."
    
def executePrint(command):
    print "Executing command type: "+"'print'"
    command=command.split()
    if(len(command)==3):
        executePrintReg(command)
    elif(len(command)==4):
        pass
    else:
        print 'Invalid print command'

#there might be a problem of what is treated as what
def executePrintReg(command): #list of strings in command
    
    regbase=command[1].lower()
    
    if regbase!='x' and regbase!='d':
        print 'Invalid print reg command'
        return
    reginfo=command[2].lower()
    
    if len(reginfo)!=2:
        print 'Invalid print reg command'
        return
    regtype=reginfo[0]
    
    if regtype!='w' and regtype!='x':
        print 'Invalid print reg command'
        return
    regnum=int(reginfo[1])
    
    if regnum<0 or regnum>31:
        print 'Invalid print reg command'
        return
    
    if regtype == 'x':
        binary=mem.regFile[regnum]
        if regbase == 'd':            
            if binary[0]=='0':
                print 'register value:' + str(int(binary,2))
            else:
                neg_binary=utilFunc.twosComplement(binary, 64)
                print 'register value: -' + str(int(neg_binary,2))
        else:
            print 'register value: ' + hex(int(binary,2))
    elif regtype == 'w':
        binary=mem.regFile[regnum][32:64]
        if regbase == 'd':            
            if binary[0]=='0':
                print 'register value:' + str(int(binary,2))
            else:
                neg_binary=utilFunc.twosComplement(binary, 32)
                print 'register value: -' + str(int(neg_binary,2))
        else:
            print 'register value: ' + hex(int(binary, 2))
            
            
def executeFlag():
    utilFunc.printAllFlags()
    
def executeRegs():
    i=0;
    for x in mem.regFile:
        print 'Register'+str(i)+': '+binaryToHexStr(x)
        i=i+1
    
def printMainHelp():
    print ''
    print '--------------------------------------------------------------------------------------------------------'
    print 'Syntax: python <PATH-TO PROJECT>/main.py [--help,--debug] [filename]'
    print 'Options: '
    print '1. --help : Prints this output. '
    print '2. --debug filename: Starts debugger for elf file with title filename'
    print '3. filename: Should be the relative/absolute path of the elf file directed towards ARMv8 architecture'
    print '--------------------------------------------------------------------------------------------------------'
    print ''
    
def executeDebuggerHelp():
    print ''
    print '------------------------------------'
    print 'Debug Options List: '
    print '1. help : Prints this output. '
    print '2. s : Runs next instruction and halt'
    print '3. c : Runs all instructions, but halts at next breakpoint'
    print '4. run : Runs all instructions till last and halt'
    print '5. break <ADDRESS> : Puts a breakpoint at the hexadecimal <ADDRESS>'
    print '6. del <ADDRESS> : Deletes the breakpoint at the hexadecimal <ADDRESS>'
    print '7. flags: Print the state of all flags'
    print '8. regs: Print the state of all registers in hex(64 binary digits)'
    print '9. print <d/x> <w/x>num: prints the decimal/hexadecimal equivalent of register(32bit/64bit) number num'
    print '10. exit: Exits the program(with the debugger)'
    print '------------------------------------'
    print ''