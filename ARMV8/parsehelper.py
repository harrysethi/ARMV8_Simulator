'''
Created on 08-Aug-2014

@author: root/abhiagar90@gmail.com
'''
import sys
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import Section
from elftools.elf.descriptions import (
    describe_ei_class, describe_ei_data, describe_ei_version,
    describe_ei_osabi, describe_e_type, describe_e_machine,
    describe_e_version_numeric, describe_p_type, describe_p_flags,
    describe_sh_type, describe_sh_flags,
    describe_symbol_type, describe_symbol_bind, describe_symbol_visibility,
    describe_symbol_shndx, describe_reloc_type, describe_dyn_tag,
    describe_ver_flags,
    )
from elftools.common.py3compat import (
        ifilter, byte2int, bytes2str, itervalues, str2bytes)

addReturn=''
numOfInst=0
little=False
PC=''

def getPC():
    global PC
    return PC

def setPC(prog_counter):
    global PC
    PC=prog_counter

def isLittle():
    global little
    return little

def process_file(filename):
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        # elfclass is a public attribute of ELFFile, read from its header
        print('%s: elfclass is %s' % (filename, elffile.elfclass))
        print(elffile.get_machine_arch())
        ss = elffile.get_section_by_name('.text')
        print ss

def _format_hex(addr, elffile, fieldsize=None, fullhex=False, lead0x=True,
                    alternate=False):
        """ Format an address into a hexadecimal string.

            fieldsize:
                Size of the hexadecimal field (with leading zeros to fit the
                address into. For example with fieldsize=8, the format will
                be %08x
                If None, the minimal required field size will be used.

            fullhex:
                If True, override fieldsize to set it to the maximal size
                needed for the elfclass

            lead0x:
                If True, leading 0x is added

            alternate:
                If True, override lead0x to emulate the alternate
                hexadecimal form specified in format string with the #
                character: only non-zero values are prefixed with 0x.
                This form is used by readelf.
        """
        if alternate:
            if addr == 0:
                lead0x = False
            else:
                lead0x = True
                fieldsize -= 2

        s = '0x' if lead0x else ''
        if fullhex:
            fieldsize = 8 if elffile.elfclass == 32 else 16
        if fieldsize is None:
            field = '%x'
        else:
            field = '%' + '0%sx' % fieldsize
        return s + field % addr


def process_2(filename):
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        


               
        
        header = elffile.header
        
        e_ident = header['e_ident']
        
        #ELF64 or ELF32
        clss=describe_ei_class(e_ident['EI_CLASS'])
        print clss
        
        #ELF Data Type Endian and complement
        data=describe_ei_data(e_ident['EI_DATA'])
        print e_ident['EI_DATA']
        print data
        print'\n'

        machinearch = describe_e_machine(header['e_machine'])
        print header['e_machine']
        print machinearch
        print '\n'

        entryadd=_format_hex(header['e_entry'],elffile)
        print header['e_entry']
        print entryadd
        
        
        
'''
        _emit('  Start of program headers:          %s' %
                header['e_phoff'])
        _emitline(' (bytes into file)')
        _emit('  Start of section headers:          %s' %
                header['e_shoff'])
        _emitline(' (bytes into file)')
        _emitline('  Flags:                             %s%s' %
                (_format_hex(header['e_flags']),
                decode_flags(header['e_flags'])))
        _emitline('  Size of this header:               %s (bytes)' %
                header['e_ehsize'])
        _emitline('  Size of program headers:           %s (bytes)' %
                header['e_phentsize'])
        _emitline('  Number of program headers:         %s' %
                header['e_phnum'])
        _emitline('  Size of section headers:           %s (bytes)' %
                header['e_shentsize'])
        _emitline('  Number of section headers:         %s' %
                header['e_shnum'])
        _emitline('  Section header string table index: %s' %
                header['e_shstrndx'])
'''


def process3(filename):
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        
        ll=elffile.iter_sections()
        
        #for x in ll:
        #    print x.name
            
        section=elffile.get_section_by_name(str2bytes('.text'))

        if section is None:
            print "ERROR! Section .text does not exist in the file!"

        #print 'Name of section is: '+bytes2str(section.name)
        
        ##assuming no reloaction section for now
        #self._note_relocs_for_section(section)
        addr = section['sh_addr']
        #print addr
        data = section.data()
        dataptr = 0

        toreturn=''
        while dataptr < len(data):
            bytesleft = len(data) - dataptr
            # chunks of 16 bytes per line
            linebytes = 16 if bytesleft > 16 else bytesleft

            toreturn+='  %s ' % _format_hex(addr, elffile, fieldsize=8 )
            for i in range(16):
                if i < linebytes:
                    toreturn+= ('%2.2x' % byte2int(data[dataptr + i]))
                else:
                    toreturn+='  '
                if i % 4 == 3:
                    toreturn+=' '

            for i in range(linebytes):
                c = data[dataptr + i : dataptr + i + 1]
                if byte2int(c[0]) >= 32 and byte2int(c[0]) < 0x7f:
                    #pass
                    #not removing not used info 
                    toreturn+=bytes2str(c)
                else:
                    #pass
                    #not removing not used info
                    toreturn+=(bytes2str(b'.'))

            toreturn+='\n'
            addr += linebytes
            dataptr += linebytes
        toreturn+='\n'
        print toreturn

def return_parsed_text_section(filename):
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        
        ll=elffile.iter_sections()
        
        #for x in ll:
        #    print x.name
            
        section=elffile.get_section_by_name(str2bytes('.text'))

        if section is None:
            print "ERROR! Section .text does not exist in the file!"

        #print 'Name of section is: '+bytes2str(section.name)
        
        ##assuming no relocation section for now
        #self._note_relocs_for_section(section)
        addr = section['sh_addr']
        data = section.data()
        dataptr = 0
        
        setStartAddress('  %s ' % _format_hex(addr, elffile, fieldsize=8 ))

        toreturn=[]
        while dataptr < len(data):
            bytesleft = len(data) - dataptr
            # chunks of 16 bytes per line
            linebytes = 16 if bytesleft > 16 else bytesleft

            #not adding addresses in beginning of 4 * 4 bytes
            #toreturn+='  %s ' % _format_hex(addr, elffile, fieldsize=8 )
            for i in range(16):
                if i < linebytes:
                    toreturn.append('%2.2x' % byte2int(data[dataptr + i]))
                else:
                    pass
                    #not doing anything
                    #toreturn+='  '
                if i % 4 == 3:
                    pass
                    #not doing anything  
                    #toreturn+=' '

            for i in range(linebytes):
                c = data[dataptr + i : dataptr + i + 1]
                if byte2int(c[0]) >= 32 and byte2int(c[0]) < 0x7f:
                    pass
                    #removing not used info 
                    #toreturn+=bytes2str(c)
                else:
                    pass
                    #removing not used info
                    #toreturn+=(bytes2str(b'.'))

            #again not adding string or newline
            #toreturn+='\n'
            addr += linebytes
            dataptr += linebytes
        #again not adding string or newline
        #toreturn+='\n'
        for x in range(len(toreturn)%4):
            toreturn.append('')
        #print toreturn        
        finalreturn= arrangeData(toreturn, isLittleEndian(elffile))
        setNumOfInst(len(finalreturn))
        return finalreturn

def fetch_PC(filename, secname='.symtab'):
    toreturn=0
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        
        section=elffile.get_section_by_name(str2bytes(secname))
        #print section['sh_entsize']
        if section['sh_entsize'] == 0:
                print("\nSymbol table '%s' has a sh_entsize of zero!" % (
                    bytes2str(section.name)))
                
        print("Symbol table '%s' contains %s entries" % (
                bytes2str(section.name), section.num_symbols()))
        
        for nsym, symbol in enumerate(section.iter_symbols()):
            if(bytes2str(symbol.name)=='_start'):
                toreturn = symbol['st_value']
                 
    setPC(toreturn)
            
def return_parsed_section(filename, secname):
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        
        ll=elffile.iter_sections()
        
        #for x in ll:
        #    print x.name
            
        section=elffile.get_section_by_name(str2bytes(secname))

        if section is None:
            print 'ERROR! Section '+secname+' does not exist in the file!'

        #print 'Name of section is: '+bytes2str(section.name)
        
        ##assuming no relocation section for now
        #self._note_relocs_for_section(section)
        addr = section['sh_addr']
        data = section.data()
        dataptr = 0
        
        
        setStartAddress('  %s ' % _format_hex(addr, elffile, fieldsize=8 ))        
                    
        toreturn=[]
        while dataptr < len(data):
            bytesleft = len(data) - dataptr
            # chunks of 16 bytes per line
            linebytes = 16 if bytesleft > 16 else bytesleft

            #not adding addresses in beginning of 4 * 4 bytes
            #toreturn+='  %s ' % _format_hex(addr, elffile, fieldsize=8 )
            for i in range(16):
                if i < linebytes:
                    toreturn.append('%2.2x' % byte2int(data[dataptr + i]))
                else:
                    pass
                    #not doing anything
                    #toreturn+='  '
                if i % 4 == 3:
                    pass
                    #not doing anything  
                    #toreturn+=' '

            for i in range(linebytes):
                c = data[dataptr + i : dataptr + i + 1]
                if byte2int(c[0]) >= 32 and byte2int(c[0]) < 0x7f:
                    pass
                    #removing not used info 
                    #toreturn+=bytes2str(c)
                else:
                    pass
                    #removing not used info
                    #toreturn+=(bytes2str(b'.'))

            #again not adding string or newline
            #toreturn+='\n'
            addr += linebytes
            dataptr += linebytes
        #again not adding string or newline
        #torreeturn+='\n'
        for x in range(len(toreturn)%4):
            toreturn.append('')
        #print toreturn        
        
        if toreturn==[]:
            print'No data to display in '+secname+' section'
            return
        global little
        little=isLittleEndian(elffile)
        finalreturn= arrangeData(toreturn, isLittleEndian(elffile))
        setNumOfInst(len(finalreturn))
        #print finalreturn
        return finalreturn
            

def isLittleEndian(elffile):
        header = elffile.header
        
        e_ident = header['e_ident']
        
        #ELF Data Type Endian and complement
        data=describe_ei_data(e_ident['EI_DATA'])
        #print data
        #print e_ident['EI_DATA']
        return data.find('little')!=-1 
        #print'\n'
        
def arrangeData(list,littleEndian):
    toreturn=[]
    if not littleEndian:
        #loop over 4 and add up
        
        for count, i in enumerate(list):
            if count % 4 == 0:
                str=list[count]+list[count+1]+list[count+2]+list[count+3]
                toreturn.append(str)
        #print toreturn
    else:
        str=list[3]+list[2]+list[1]+list[0]
        toreturn.append(str)
        for count, i in enumerate(list):
            if count % 4 == 0 and count != 0:
                str=list[count+3]+list[count+2]+list[count+1]+list[count]
                toreturn.append(str)
    return toreturn


def setStartAddress(add):
    global addReturn
    addReturn=add
    
def getStartAddress():
    return addReturn
    
def getNumOfInst():
    return numOfInst
    
def setNumOfInst(num):
    global numOfInst
    numOfInst =  num
    
def getNumOfBytes():
    return getNumOfInst()*4


#assuming if called from arg line then pass file name as pass a file name from the calling method
if __name__ == '__main__':
        filename = sys.argv[1]        
        #process3(filename)
        fetch_PC(filename,'.symtab')
        print getPC()
                 
        #print getStartAddress()
        #print getNumOfInst()
        #print getNumOfBytes()