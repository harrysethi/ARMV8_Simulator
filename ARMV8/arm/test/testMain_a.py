'''
Created on Aug 8, 2014

@author: harinder
'''

from arm.execute import decoder
from arm.utils.utilFunc import printAllRegs, printAllFlags
    
def main():
    print "Inside Main"
    hexCode = "0a020020"   
    decoder.decodeInstr(hexCode) 
    printAllRegs()
    printAllFlags()
main()
