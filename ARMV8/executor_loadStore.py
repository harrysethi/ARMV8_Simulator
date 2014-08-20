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
        
    offset = utilFunc.signExtend(imm19+'00',64)
        
    address = armdebug.getPC() + offset
    #Data size : size*8
    
    if(memOp == 'Load'):
        #data = mem.
        '''write function-------------------------------------'''
    
    if(signed):
        data = utilFunc.signExtend(data,64)
    utilFunc.setRegValue(rtKey,data, '0')
    

#---Load Register (Literal)---
def execLDR_l32(binary):
    helper_l(binary)

def execLDR_l64(binary):
    helper_l(binary)
    
def execLDRSW_l(binary):
    helper_l(binary)
    
    
#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_posti_32(binary):
    '''Not implemented yet'''
    
def execLDP_rp_posti_32(binary):
    '''Not implemented yet'''
    
def execSTP_rp_posti_64(binary):
    '''Not implemented yet'''
    
def execLDP_rp_posti_64(binary):
    '''Not implemented yet'''
    
    
#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_prei_32(binary):
    '''Not implemented yet'''
    
def execLDP_rp_prei_32(binary):
    '''Not implemented yet'''
    
def execSTP_rp_prei_64(binary):
    '''Not implemented yet'''
    
def execLDP_rp_prei_64(binary):
    '''Not implemented yet'''


#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_offset_32(binary):
    '''Not implemented yet'''
    
def execLDP_rp_offset_32(binary):
    '''Not implemented yet'''
    
def execSTP_rp_offset_64(binary):
    '''Not implemented yet'''
    
def execLDP_rp_offset_64(binary):
    '''Not implemented yet'''


def helper_reg(binary):
    instr = ''
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    s = binary[19]
    option = binary[16,19]
    opc = binary[8,10]
    
    wback = false
    postIndex = false
    scale = utilFunc.uInt(size)
    if s=='1':
        shift = scale
    else:
        shift = 0
        
    if(opc[0] == '0'):
        if(opc[1] == '1'):
            memOp = 'Load'
        else:
            memOp = 'Store'
        if(size == '11'):
            regSize = 64
        else:
            regSize = 32
        signed = false
    else:
        if(size == '11'):
            memOp = 'Prefetch'
        else:
            memOp = 'Load'
            if opc[1] == '1':
                regSize = 32
            else:
                regSize = 64
            signed = true
            
    dataSize = 8 << scale
    
    offset, instr = utilFunc.extendReg(rmVal, shift, option, instr, 64)
    #wb_unknown = false
    #rt_unknown = false
    
    address = utilFunc.getRegValueByStringkey(rnKey, '1')
    if not(postindex):
        address = address + offset
        
    if(memOp == 'Store'):
        data = utilFunc.getRegValueByStringkey(rtKey, '0')
        mem.storeWordToMemory(address, data)
    elif(memOP == 'Load'):
        #data =
        '''--------------------to be implemented...calling a function----------------'''
        if(signed):
            utilFunc.setRegValue(rtKey, utilFunc.signExtend(data,regSize),'0')
        else:
            utilFunc.setRegValue(rtKey, utilFunc.zeroExtend(data,regSize),'0')
    
    if(wback):
        if postIndex:
            address = address + offset
        utilFunc.setRegValue(rnKey, address,'1')
    
def helper_imm():
    if(opc[0] == '0'):
        if(opc[1] == '1'):
            memOp = 'Load'
        else:
            memOp = 'Store'
        if(size == '11'):
            regSize = 64
        else:
            regSize = 32
        signed = false
    else:
        if(size == '11'):
            memOp = 'Prefetch'
        else:
            memOp = 'Load'
            if opc[1] == '1':
                regSize = 32
            else:
                regSize = 64
            signed = true
            
    dataSize = 8 << scale
    
    ###offset, instr = utilFunc.extendReg(rmVal, shift, option, instr, 64)  ---> not used
    #wb_unknown = false
    #rt_unknown = false
    
    address = utilFunc.getRegValueByStringkey(rnKey, '1')
    if not(postindex):
        address = address + offset
        
    if(memOp == 'Store'):
        data = utilFunc.getRegValueByStringkey(rtKey, '0')
        mem.storeWordToMemory(address, data)
    elif(memOP == 'Load'):
        #data =
        '''--------------------to be implemented...calling a function----------------'''
        if(signed):
            utilFunc.setRegValue(rtKey, utilFunc.signExtend(data,regSize),'0')
        else:
            utilFunc.setRegValue(rtKey, utilFunc.zeroExtend(data,regSize),'0')
    
    if(wback):
        if postIndex:
            address = address + offset
        utilFunc.setRegValue(rnKey, address,'1')
    
#---Load/Store Register (Post-Indexed Immediate)---    
def execSTR_reg_posti_32(binary):
    instr = ''
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    imm9 = binary[11,20]
    opc = binary[8,10]
    
    
    wback = true
    postIndex = true
    scale = utilFunc.uInt(size)
    offset = utilFunc.signExtend(imm9,64)
    
def execLDR_reg_posti_32(binary):
    '''Not implemented yet'''
    
def execLDRSW_reg_posti(binary):
    '''Not implemented yet'''
    
def execSTR_reg_posti_64(binary):
    '''Not implemented yet'''

def execLDR_reg_posti_64(binary):
    '''Not implemented yet'''


#---Load/Store Register (Pre-Indexed Immediate)---    
def execSTR_reg_prei_32(binary):
    instr = ''
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    imm9 = binary[11,20]
    opc = binary[8,10]
    
    wback = true
    postIndex = false
    scale = utilFunc.uInt(size)
    offset = utilFunc.signExtend(imm9,64)
    
def execLDR_reg_prei_32(binary):
    '''Not implemented yet'''
    
def execLDRSW_reg_prei(binary):
    '''Not implemented yet'''
    
def execSTR_reg_prei_64(binary):
    '''Not implemented yet'''

def execLDR_reg_prei_64(binary):
    '''Not implemented yet'''
    

#---Load/Store Register (Register offset)---    
def execSTR_reg_offset_32(binary):
    instr = ''
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    imm12 = binary[10,22]
    opc = binary[8,10]
    
    wback = false
    postIndex = false
    scale = utilFunc.uInt(size)
    offset = utilFunc.lsl(utilFunc.zeroExtend(imm12,64),scale)
    
def execLDR_reg_offset_32(binary):
    pass
    
def execLDRSW_reg_offset(binary):
    '''Not implemented yet'''
    
def execSTR_reg_offset_64(binary):
    '''Not implemented yet'''

def execLDR_reg_offset_64(binary):
    '''Not implemented yet'''
    

#---Load/Store Register (Unsigned Immediate)---    
def execSTR_reg_unsignedi_32(binary):
    '''Not implemented yet'''
    
def execLDR_reg_unsignedi_32(binary):
    '''Not implemented yet'''
    
def execLDRSW_reg_unsignedi(binary):
    '''Not implemented yet'''
    
def execSTR_reg_unsignedi_64(binary):
    '''Not implemented yet'''

def execLDR_reg_unsignedi_64(binary):
    '''Not implemented yet'''