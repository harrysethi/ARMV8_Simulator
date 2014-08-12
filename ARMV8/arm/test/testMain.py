'''
Created on Aug 8, 2014

@author: harinder
'''

from arm.execute import decoder
from arm.parse import parsehelper
import sys
from arm.utils.utilFunc import resetInstrFlag, printAllRegs, printAllFlags

if __name__ == '__main__':
        #filename = sys.argv[1]
        filename='/home/harinder/Desktop/testcase4_mov/a.out'     
        #process3(filename)
        hexes=parsehelper.return_parsed_text_section(filename)
        print hexes
        print "Inside Main"
        #hexCode = "52800141" 
        for hexcode in hexes:
            resetInstrFlag()
            decoder.decodeInstr(hexcode)        	 
        printAllRegs()
        printAllFlags()