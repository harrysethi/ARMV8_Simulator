'''
Created on Aug 8, 2014

@author: abhiagar90
'''

import decoder
from utilFunc import resetInstrFlag, printAllRegs, printAllFlags

            
def main():
    print "---Started---"
    #"52800102"
    hexes = ["531f7841"]
    for hexcode in hexes:
        resetInstrFlag()
        decoder.decodeInstr(hexcode)
    printAllRegs()
    printAllFlags()
        
main()