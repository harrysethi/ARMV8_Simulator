'''
@author: abhiagar90
'''

import decoder
from utilFunc import resetInstrFlag, printAllRegs, printAllFlags

            
def main():
    print "---Started---"
    #"52800102"
    hexes = ["d503201f"]
    for hexcode in hexes:
        resetInstrFlag()
        decoder.decodeInstr(hexcode)
    printAllRegs()
    printAllFlags()
        
main()