'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc

def helper_l(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    imm19 = binary[8:27]
    opc = binary[0:2]
    signed = False
    
    if(opc == '00'):
        size = 4
    elif(opc == '01'):
        size = 8
    elif(opc == '10'):
        size = 4
        signed = True
        
    offset = utilFunc.signExtend(imm19 + '00', 64)
    offset = utilFunc.sInt(offset, 64)
        
    address = armdebug.getPC() + offset
    dataSize = size * 8
    
    data = utilFunc.fetchFromMemory(address, dataSize)
    
    if(data == const.TRAP):
            utilFunc.finalize_simple(instr)
            print "HEY!!! There seems to be a problem - memory location can not be accessed"
            print "Moving ahead without executing the instruction"
            return
    
    if(signed):
        data = utilFunc.signExtend(data, 64)
    instr += str(rtKey) + ", #" + str(offset)
    utilFunc.finalize(rtKey, data.zfill(64), instr, '0')
    

#---Load Register (Literal)---
def execLDR_l32(binary):    
    helper_l(binary, 'LDR w')

def execLDR_l64(binary):
    helper_l(binary, 'LDR w')
    
def execLDRSW_l(binary):
    helper_l(binary, 'LDRSW x')
    
 

def helper_rp_posti(binary, instr):
    helper_rp(True, True, binary, instr)
    
def helper_rp_prei(binary, instr):
    helper_rp(True, False, binary, instr)
    
def helper_rp_offset(binary, instr):
    helper_rp(False, False, binary, instr)
    
def helper_rp(wback, postIndex, binary, instr):
     rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
     rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
     rt2Key = utilFunc.getRegKeyByStringKey(binary[17:22])
     
     imm7 = binary[10:17]
     l = binary[9]     
     opc = binary[0:2]
     
     if(l == '1'):
         memOp = const.MEM_OP_LOAD
     else:
         memOp = const.MEM_OP_STORE

     signed = (opc[1] != '0')
     scale = 2 + utilFunc.uInt(opc[0])
     
     dataSize = 8 << scale
     offset = utilFunc.lsl(utilFunc.signExtend(imm7, 64), scale)
     
     dbytes = datasize / 8;
     
     address = utilFunc.getRegValueByStringkey(binary[22:27], '1')
     address = utilFunc.uInt(address, 64)
     
     if not(postIndex):
        address = address + offset
     
     if(memOp == const.MEM_OP_STORE):
        data1 = utilFunc.getRegValueByStringkey(binary[27:32], '0')
        data2 = utilFunc.getRegValueByStringkey(binary[17:22], '0')  
        utilFunc.storeToMemory(data1, address, dataSize)
        utilFunc.storeToMemory(data2, address + dbytes, dataSize)
             
     elif(memOp == const.MEM_OP_LOAD):
        data1 = utilFunc.fetchFromMemory(address, dataSize)
        data2 = utilFunc.fetchFromMemory(address + dbytes, dataSize)
        
        if(data1 == const.TRAP or data2 == const.TRAP):
            utilFunc.finalize_simple(instr)
            print "HEY!!! There seems to be a problem - memory location can not be accessed"
            print "Moving ahead without executing the instruction"
            return
        
        if(signed):
            data1 = utilFunc.signExtend(data1, 64)
            data2 = utilFunc.signExtend(data2, 64)
            
        utilFunc.setRegValue(rtKey, data1.zfill(64), '0')
        utilFunc.setRegValue(rt2Key, data2.zfill(64), '0')
     
     if(wback):       
         if postIndex:
            address = address + offset
            address = utilFunc.intToBinary(address, 64)
         utilFunc.setRegValue(rnKey, address, '1')
    
     type = binary[7:9]
     if(opc == '00'):
         r = 'w'
     if(opc == '10'):
         r = 'x'
            
     if(type == 01):
         #Post-index
         instr += " " + r + str(rtKey) +", " + r + str(rt2Key) + ", [x" + str(rnKey) + "], #" + str(offset) 
     if(type == 11):
         #Pre-index
         instr += " " + r + str(rtKey) +", " + r + str(rt2Key) + ", [x" + str(rnKey) + ", #" + str(offset) + "]!"   
     if(type == 10):
         #Signed-offset
         instr += " " + r + str(rtKey) +", " + r + str(rt2Key) + ", [x" + str(rnKey) + ", #" + str(offset) + "]"
     utilFunc.finalize_simple(instr)
    
    
#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_posti_32(binary):
    helper_rp_posti(binary, 'STP')
    
def execLDP_rp_posti_32(binary):
    helper_rp_posti(binary, 'LDP')
    
def execSTP_rp_posti_64(binary):
    helper_rp_posti(binary, 'STP')
    
def execLDP_rp_posti_64(binary):
    helper_rp_posti(binary, 'LDP')
     
#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_prei_32(binary):
    helper_rp_prei(binary, 'STP')
    
def execLDP_rp_prei_32(binary):
    helper_rp_prei(binary, 'LDP')
    
def execSTP_rp_prei_64(binary):
    helper_rp_prei(binary, 'STP')
    
def execLDP_rp_prei_64(binary):
    helper_rp_prei(binary, 'LDP')


#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def execLDP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def execSTP_rp_offset_64(binary):
    helper_rp_offset(binary, 'STP')
    
def execLDP_rp_offset_64(binary):
    helper_rp_offset(binary, 'LDP')


    
#---Load/Store Register (Post-Indexed Immediate)---    
def execSTR_reg_posti_32(binary):
    helper_reg_posti(binary, 'STR w')
    
def execLDR_reg_posti_32(binary):
    helper_reg_posti(binary, 'LDR w')
    
def execLDRSW_reg_posti(binary):
    helper_reg_posti(binary, 'LDRSW x')
    
def execSTR_reg_posti_64(binary):
    helper_reg_posti(binary, 'STR x')

def execLDR_reg_posti_64(binary):
    helper_reg_posti(binary, 'LDR x')


#---Load/Store Register (Pre-Indexed Immediate)---    
def execSTR_reg_prei_32(binary):
    helper_reg_prei(binary, 'STR w')
    
def execLDR_reg_prei_32(binary):
    helper_reg_prei(binary, 'LDR w')
    
def execLDRSW_reg_prei(binary):
    helper_reg_prei(binary, 'LDRS x')
    
def execSTR_reg_prei_64(binary):
    helper_reg_prei(binary, 'STR x')

def execLDR_reg_prei_64(binary):
    helper_reg_prei(binary, 'LDR x')


#---Load/Store Register (Unsigned Offset)---    
def execSTR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'STR w')
    
def execLDR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'LDR w')
    
def execLDRSW_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRSW x')
    
def execSTR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'STR x')

def execLDR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'LDR x')



#---Load/Store Register (Register offset)---    
def execSTR_reg_offset_32(binary):
    helper_reg(binary, 'STR w')
    
def execLDR_reg_offset_32(binary):
    helper_reg(binary, 'LDR w')
    
def execLDRSW_reg_offset(binary):
    helper_reg(binary, 'LDRSW x')
    
def execSTR_reg_offset_64(binary):
    helper_reg(binary, 'STR x')

def execLDR_reg_offset_64(binary):
    helper_reg(binary, 'LDR x')
    

    
def helper_reg_posti(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    imm9 = binary[11:20]
    opc = binary[8:10]
    size = binary[0:2]
    wback = True
    postIndex = True
    scale = utilFunc.uInt(size)
    offset = utilFunc.signExtend(imm9, 64)
    offset = utilFunc.sInt(offset, 64)
    instr += str(rtKey) + ", [x" + str(rnKey) + "], #" + str(offset) 
    helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)

def helper_reg_prei(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    imm9 = binary[11:20]
    opc = binary[8:10]
    size = binary[0:2]
    wback = True
    postIndex = False
    scale = utilFunc.uInt(size)
    offset = utilFunc.signExtend(imm9, 64)
    offset = utilFunc.sInt(offset, 64)
    instr += str(rtKey) + ", [x" + str(rnKey) + ", #" + str(offset) + "]!"
    helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)

def helper_reg_unsignedOffset(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    imm12 = binary[10:22]
    opc = binary[8:10]
    size = binary[0:2]
    wback = False
    postIndex = False
    scale = utilFunc.uInt(size)
    offset = utilFunc.lsl(utilFunc.zeroExtend(imm12, 64), scale)
    offset = utilFunc.sInt(offset, 64)
    instr += str(rtKey) + ", [x" + str(rnKey) + ", #" + str(offset) + "]"
    helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)

def helper_reg(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    s = binary[19]
    option = binary[16:19]
    opc = binary[8:10]
    size = binary[0:2]
    
    wback = False
    postIndex = False
    scale = utilFunc.uInt(size)
    if s == '1':
        shift = scale
    else:
        shift = 0
    
    if(option[1:3] == '10'):
        rmToPrint = 'w'
        rmVal = rmVal[32:64]
    elif(option[1:3] == '11'):
        rmToPrint = 'x'
        
    instr += str(rtKey) + ", [x" + str(rnKey) + ", " + rmToPrint + str(rmKey) + ", "     
    offset, instr = utilFunc.extendReg(rmVal, shift, option, instr, 64)
    
    instr += ' #'
    if size == '10':
        if s == '0':
            instr += '0'
        else:
            instr += '2'
            
    if size == '11':
        if s == '0':
            instr += '0'
        else:
            instr += '3'
    instr += ']'
    
    helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)    

    
def helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr):
    if(opc[0] == '0'):
        if(opc[1] == '1'):
            memOp = const.MEM_OP_LOAD
        else:
            memOp = const.MEM_OP_STORE
        if(size == '11'):
            regSize = 64
        else:
            regSize = 32
        signed = False
    else:
        if(size == '11'):
            memOp = const.MEM_OP_PREFETCH
        else:
            memOp = const.MEM_OP_LOAD
            if opc[1] == '1':
                regSize = 32
            else:
                regSize = 64
            signed = True
            
    dataSize = 8 << scale
    
    '''wb_unknown = False
    rt_unknown = False'''  # commenting - assuming them to be false always 
    
    address = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    address = utilFunc.uInt(address)
    if not(postIndex):
        address = address + offset
        
    if(memOp == const.MEM_OP_STORE):
        data = utilFunc.getRegValueByStringkey(binary[27:32], '0')
        utilFunc.storeToMemory(data, address, dataSize)
            
    elif(memOp == const.MEM_OP_LOAD):
        data = utilFunc.fetchFromMemory(address, dataSize)
        if(data == const.TRAP):
            utilFunc.finalize_simple(instr)
            print "HEY!!! There seems to be a problem - memory location can not be accessed"
            print "Moving ahead without executing the instruction"            
            return   
        if(signed):
            data = utilFunc.signExtend(data, regSize)
        else:
            data = utilFunc.zeroExtend(data, regSize)
            
    utilFunc.setRegValue(rtKey, data.zfill(64), '0')
        
    if(wback):
        if postIndex:
            address = address + offset
            address = utilFunc.intToBinary(address, 64)
        utilFunc.setRegValue(rnKey, address, '1')
    
    utilFunc.finalize_simple(instr)
