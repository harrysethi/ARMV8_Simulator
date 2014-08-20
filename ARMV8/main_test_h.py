'''
@author: abhiagar90
'''

import decoder
from utilFunc import resetInstrFlag, printAllRegs, printAllFlags


def main():
    print "---Started---"
    hexes = ["f8402061"]

    for hexcode in hexes:
        resetInstrFlag()
        decoder.decodeInstr(hexcode)
    printAllRegs()
    printAllFlags()

main()
