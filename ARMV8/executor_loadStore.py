'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc

def helper_l(binary):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    imm19 = binary[8:27]
    opc = binary[0:2]
    signed = false
    
    if(opc == '00'):
        size = 4
    elif(opc == '01'):
        size = 8
    elif(opc == '10'):
        size = 4
        signed = true
        
    offset = utilFunc.signExtend(imm19 + '00', 64)
    offset = utilFunc.sInt(offset, 64)
        
    address = armdebug.getPC() + offset
    dataSize = size * 8
    
    if(memOp == 'Load'):
       data = utilFunc.fetchFromMemory(address, dataSize)        
    
    if(signed):
        data = utilFunc.signExtend(data, 64)
    utilFunc.setRegValue(rtKey, data.zfill(64), '0')
    

#---Load Register (Literal)---
def execLDR_l32(binary):
    helper_l(binary)

def execLDR_l64(binary):
    helper_l(binary)
    
def execLDRSW_l(binary):
    helper_l(binary)
    
 

def helper_rp_posti(binary):
    wback = true
    postIndex= true
    
def helper_rp_prei(binary):
    wback = true
    postIndex= false
    
def helper_rp_offset(binary): 
    wback = false
    postIndex= false
    
#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_posti_32(binary):
    helper_rp_posti(binary)
    
def execLDP_rp_posti_32(binary):
    helper_rp_posti(binary)
    
def execSTP_rp_posti_64(binary):
    helper_rp_posti(binary)
    
def execLDP_rp_posti_64(binary):
    helper_rp_posti(binary)
     
#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_prei_32(binary):
    helper_rp_prei(binary)
    
def execLDP_rp_prei_32(binary):
    helper_rp_prei(binary)
    
def execSTP_rp_prei_64(binary):
    helper_rp_prei(binary)
    
def execLDP_rp_prei_64(binary):
    helper_rp_prei(binary)


#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_offset_32(binary):
    helper_rp_offset(binary)
    
def execLDP_rp_offset_32(binary):
    helper_rp_offset(binary)
    
def execSTP_rp_offset_64(binary):
    helper_rp_offset(binary)
    
def execLDP_rp_offset_64(binary):
    helper_rp_offset(binary)


    
#---Load/Store Register (Post-Indexed Immediate)---    
def execSTR_reg_posti_32(binary):
    helper_reg_posti(binary)
    
def execLDR_reg_posti_32(binary):
    helper_reg_posti(binary)
    
def execLDRSW_reg_posti(binary):
    helper_reg_posti(binary)
    
def execSTR_reg_posti_64(binary):
    helper_reg_posti(binary)

def execLDR_reg_posti_64(binary):
    helper_reg_posti(binary)


#---Load/Store Register (Pre-Indexed Immediate)---    
def execSTR_reg_prei_32(binary):
    helper_reg_prei(binary)
    
def execLDR_reg_prei_32(binary):
    helper_reg_prei(binary)
    
def execLDRSW_reg_prei(binary):
    helper_reg_prei(binary)
    
def execSTR_reg_prei_64(binary):
    helper_reg_prei(binary)

def execLDR_reg_prei_64(binary):
    helper_reg_prei(binary)


#---Load/Store Register (Unsigned Offset)---    
def execSTR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary)
    
def execLDR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary)
    
def execLDRSW_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary)
    
def execSTR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary)

def execLDR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary)



#---Load/Store Register (Register offset)---    
def execSTR_reg_offset_32(binary):
    helper_reg(binary)
    
def execLDR_reg_offset_32(binary):
    helper_reg(binary)
    
def execLDRSW_reg_offset(binary):
    helper_reg(binary)
    
def execSTR_reg_offset_64(binary):
    helper_reg(binary)

def execLDR_reg_offset_64(binary):
    helper_reg(binary)
    

    
def helper_reg_posti(binary):
    instr = ''
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    imm9 = binary[11:20]
    opc = binary[8:10]
    size = binary[0:2]
    wback = true
    postIndex = true
    scale = utilFunc.uInt(size)
    offset = utilFunc.signExtend(imm9, 64)
    offset = utilFunc.sInt(offset, 64)
    helper_all(opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)

def helper_reg_prei(binary):
    instr = ''
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    imm9 = binary[11:20]
    opc = binary[8:10]
    size = binary[0:2]
    wback = true
    postIndex = false
    scale = utilFunc.uInt(size)
    offset = utilFunc.signExtend(imm9, 64)
    offset = utilFunc.sInt(offset, 64)
    helper_all(opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)

def helper_reg_unsignedOffset(binary):
    instr = ''
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    imm12 = binary[10:22]
    opc = binary[8:10]
    size = binary[0:2]
    wback = false
    postIndex = false
    scale = utilFunc.uInt(size)
    offset = utilFunc.lsl(utilFunc.zeroExtend(imm12, 64), scale)
    offset = utilFunc.sInt(offset, 64)
    helper_all(opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)

def helper_reg(binary):
    instr = ''
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    s = binary[19]
    option = binary[16:19]
    opc = binary[8:10]
    size = binary[0:2]
    
    wback = false
    postIndex = false
    scale = utilFunc.uInt(size)
    if s == '1':
        shift = scale
    else:
        shift = 0
        
    offset, instr = utilFunc.extendReg(rmVal, shift, option, instr, 64)    
    helper_all(opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)    

    
def helper_all(opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr):
    if(opc[0] == '0'):
        if(opc[1] == '1'):
            memOp = const.MEM_OP_LOAD
        else:
            memOp = const.MEM_OP_STORE
        if(size == '11'):
            regSize = 64
        else:
            regSize = 32
        signed = false
    else:
        if(size == '11'):
            memOp = const.MEM_OP_PREFETCH
        else:
            memOp = const.MEM_OP_LOAD
            if opc[1] == '1':
                regSize = 32
            else:
                regSize = 64
            signed = true
            
    dataSize = 8 << scale
    
    '''wb_unknown = false
    rt_unknown = false'''  # commenting - assuming them to be false always 
    
    address = utilFunc.getRegValueByStringkey(rnKey, '1')
    address = utilFunc.uInt(address, 64)
    if not(postindex):
        address = address + offset
        
    if(memOp == const.MEM_OP_STORE):
        data = utilFunc.getRegValueByStringkey(rtKey, '0')
        storeToMemory(data, address, dataSize)
            
    elif(memOP == const.MEM_OP_LOAD):
        data = utilFunc.fetchFromMemory(address, dataSize)        
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
