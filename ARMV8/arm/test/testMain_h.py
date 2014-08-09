'''
Created on Aug 8, 2014

@author: harinder
'''

from arm.utils.mem import regFile
from arm.execute import decoder
from arm.utils.utilFunc import resetInstrFlag
        
def main():
    print "Inside Main"
    #52800061,528000a2,0a020020
    hexes = ["52800061","528000a2","0a020020"]
    for hexcode in hexes:
        resetInstrFlag()
        decoder.decodeInstr(hexcode)
    for x in regFile:
        print x
        
main()
