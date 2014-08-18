'''
@author: abhiagar90
'''

import decoder
from utilFunc import resetInstrFlag, printAllRegs, printAllFlags


def main():
    print "---Started---"
    hexes = ["12800042", "b27ef7e1"]
    for hexcode in hexes:
        resetInstrFlag()
        decoder.decodeInstr(hexcode)
    printAllRegs()
    printAllFlags()

main()
