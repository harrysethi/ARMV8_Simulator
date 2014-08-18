'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc

def helper_l():
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    imm19 = binary[8:27]
    opc = binary[0:2]
    signed = false
    
    if(opc == '00'):
        size = 4
    elif(opc == '01'):
        size = 8
        
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
    pass

def execLDR_l64(binary):
    '''Not implemented yet'''
    
def execLDRSW_l(binary):
    '''Not implemented yet'''
    
    
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


#---Load/Store Register (Post-Indexed Immediate)---    
def execSTR_reg_posti_32(binary):
    '''Not implemented yet'''
    
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
    '''Not implemented yet'''
    
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
    '''Not implemented yet'''
    
def execLDR_reg_offset_32(binary):
    '''Not implemented yet'''
    
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