'''
Created on Aug 8, 2014

@author: harinder
'''

from arm.utils.mem import regFile
from arm.execute import decoder
from arm.parse import parsehelper
import sys

if __name__ == '__main__':
        #filename = sys.argv[1]
        filename='/home/harinder/Desktop/testcase4_mov/a.out'     
        #process3(filename)
        hexes=parsehelper.return_parsed_text_section(filename)
        print hexes
        print "Inside Main"
        #hexCode = "52800141" 
        for hexcode in hexes:
        	decoder.decodeInstr(hexcode) 
        for x in regFile:
            print x
        
def main():
    print "Inside Main"
    hexCode = "52800141"   
    decoder.decodeInstr(hexCode) 
    for x in regFile:
        print x
        
#main()
