'''
Created on Aug 8, 2014

@author: harinder
'''

from arm.execute import decoder

from arm.utils.utilFunc import printAllRegs, printAllFlags

from arm.parse import parsehelper
from arm.utils.utilFunc import resetInstrFlag
from arm.debugger import armdebug
from arm.debugger.armdebug import isDebugMode

    
if __name__ == '__main__':
        #filename = sys.argv[1]
        filename='/root/Desktop/softwaresystems/gcc-linaro-aarch64-linux-gnu-4.9-2014.07_linux/bin/a.out'     

        hexes=parsehelper.return_parsed_text_section(filename)
        print hexes
        print "Inside Main"
        #hexCode = "52800141" 
        
        #let's start the debug mode
        armdebug.startDebugMode()
        armdebug.setHexes(hexes)
        print armdebug.isDebugMode()
        
        if isDebugMode:
            #get commands till the user writes exit
            #for each command call execute command
            #hexes is where our insts are
            armdebug.startInteraction()
        else:        
            for hexcode in hexes:
                resetInstrFlag()
                decoder.decodeInstr(hexcode)             
            for x in regFile:
                    print x
        print 'And the starting address was: ' + parsehelper.getStartAddress()
            
def main():
    print "Inside Main"
    hexCode = "0a020020"   
    decoder.decodeInstr(hexCode) 
    printAllRegs()
    printAllFlags()
        
#main()

