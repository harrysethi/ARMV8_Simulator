'''
Created on Aug 8, 2014

@author: abhiagar90
'''

import decoder
from utilFunc import resetInstrFlag, printAllRegs, printAllFlags
import utilFunc

            
def main():
    print "---Started---"
    #"52800102"
    hexes = ["5400002e","528000e2","17fffffe"]
    for hexcode in hexes:
        resetInstrFlag()
        utilFunc.set_Z_flag()
        decoder.decodeInstr(hexcode)
    printAllRegs()
    printAllFlags()
        
main()