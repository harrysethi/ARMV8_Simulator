'''
Created on Aug 8, 2014

@author: harinder
'''

from arm.utils.mem import regFile
from arm.execute import decoder
    
def main():
    print "Inside Main"
    hexCode = "0a020020"   
    decoder.decodeInstr(hexCode) 
    for x in regFile:
        print x
        
main()
