'''
Created on Aug 8, 2014

@author: harinder
'''

from arm.execute import decoder
from arm.utils.utilFunc import resetInstrFlag, printAllFlags, printAllRegs

def main():
    print "Inside Main"
    hexes = ["52800102","52800021","2b017c43"]
    for hexcode in hexes:
        resetInstrFlag()
        decoder.decodeInstr(hexcode)
    printAllRegs()
    printAllFlags()

main()
