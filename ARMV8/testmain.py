'''
Created on Aug 8, 2014

@author: abhiagar90
'''

import decoder
import os


import parsehelper
import armdebug
from armdebug import isDebugMode, executeRegs, executeFlag
from utilFunc import resetInstrFlag, printAllRegs, printAllFlags
from mem import regFile
import sys

    
if __name__ == '__main__':
    
        filename=''
        
        try:
            hexes=parsehelper.return_parsed_text_section(filename)
        except:
            print "He's dead Larry." 
            print "The inputfile seems to be a not compatibe ARMv8 elf."
            sys.exit(0)
        
        if isDebugMode():
            armdebug.setHexes(hexes)
            armdebug.startInteraction()
        else:        
            for hexcode in hexes:
                resetInstrFlag()
                decoder.decodeInstr(hexcode)             
            executeRegs()
            executeFlag()
        
'''            
def main():
    print "Inside Main"
    hexCode = "0a020020"   
    decoder.decodeInstr(hexCode) 
    printAllRegs()
    printAllFlags()
        
#main()'''