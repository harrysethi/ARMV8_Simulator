'''
@author: abhiagar90
'''

import decoder
from utilFunc import resetInstrFlag, printAllRegs, printAllFlags


def main():
    print "---Started---"
    hexes = ["d2817702", "9342fc41"]
    for hexcode in hexes:
        resetInstrFlag()
        decoder.decodeInstr(hexcode)
    printAllRegs()
    printAllFlags()

main()
