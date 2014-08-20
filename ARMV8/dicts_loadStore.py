'''
@author: harinder
'''
import executor_loadStore

def INSTRUCTION_TYPE(binary,i):
    try:
        return {
            0 : LOAD_REGISTER_LITERAL,
            1 : LOAD_STORE_REGISTER_PAIR_POSTINDEXED,
            2 : LOAD_STORE_REGISTER_PAIR_PREINDEXED,
            3 : LOAD_STORE_REGISTER_PAIR_SIGNED_OFFSET,
            4 : LOAD_STORE_REGISTER_POSTINDEXED_IMMEDIATE,
            5 : LOAD_STORE_REGISTER_PREINDEXED_IMMEDIATE,
            6 : LOAD_STORE_REGISTER_UNSIGNED_OFFSET,
            7 : LOAD_STORE_REGISTER_OFFSET,
        }[i](binary)
    except KeyError:
        i=i

    
def LOAD_REGISTER_LITERAL(binary):
    key = binary[0:8]
    return {       
       "00011000" : executor_loadStore.execLDR_l32,
       "01011000" : executor_loadStore.execLDR_l64,
       "10011000" : executor_loadStore.execLDRSW_l,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PAIR_POSTINDEXED(binary):
    key = binary[0:10]
    return {       
       "0010100010" : executor_loadStore.execSTP_rp_posti_32,
       "0010100011" : executor_loadStore.execLDP_rp_posti_32,
       "1010100010" : executor_loadStore.execSTP_rp_posti_64,
       "1010100011" : executor_loadStore.execLDP_rp_posti_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PAIR_PREINDEXED(binary):
    key = binary[0:10]
    return {       
       "0010100110" : executor_loadStore.execSTP_rp_prei_32,
       "0010100111" : executor_loadStore.execLDP_rp_prei_32,
       "1010100110" : executor_loadStore.execSTP_rp_prei_64,
       "1010100111" : executor_loadStore.execLDP_rp_prei_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PAIR_SIGNED_OFFSET(binary):
    key = binary[0:10]
    return {       
       "0010100100" : executor_loadStore.execSTP_rp_offset_32,
       "0010100101" : executor_loadStore.execLDP_rp_offset_32,
       "1010100100" : executor_loadStore.execSTP_rp_offset_64,
       "1010100101" : executor_loadStore.execLDP_rp_offset_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_POSTINDEXED_IMMEDIATE(binary):
    key = binary[0:11]+"-"*9+binary[20:22]
    return {       
       "10111000000"+"-"*9+"01" : executor_loadStore.execSTR_reg_posti_32,
       "10111000010"+"-"*9+"01" : executor_loadStore.execLDR_reg_posti_32,
       "10111000100"+"-"*9+"01" : executor_loadStore.execLDRSW_reg_posti,
       "11111000000"+"-"*9+"01" : executor_loadStore.execSTR_reg_posti_64,
       "11111000010"+"-"*9+"01" : executor_loadStore.execLDR_reg_posti_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PREINDEXED_IMMEDIATE(binary):
    key = binary[0:11]+"-"*9+binary[20:22]
    return {       
       "10111000000"+"-"*9+"11" : executor_loadStore.execSTR_reg_prei_32,
       "10111000010"+"-"*9+"11" : executor_loadStore.execLDR_reg_prei_32,
       "10111000100"+"-"*9+"11" : executor_loadStore.execLDRSW_reg_prei,
       "11111000000"+"-"*9+"11" : executor_loadStore.execSTR_reg_prei_64,
       "11111000010"+"-"*9+"11" : executor_loadStore.execLDR_reg_prei_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_UNSIGNED_OFFSET(binary):
    key = binary[0:10]
    return {       
       "1011100100" : executor_loadStore.execSTR_reg_unsignedOffset_32,
       "1011100101" : executor_loadStore.execLDR_reg_unsignedOffset_32,
       "1011100110" : executor_loadStore.execLDRSW_reg_unsignedOffset,
       "1111100100" : executor_loadStore.execSTR_reg_unsignedOffset_64,
       "1111100101" : executor_loadStore.execLDR_reg_unsignedOffset_64,
    }[key](binary)
    
    
def LOAD_STORE_REGISTER_OFFSET(binary):
    key = binary[0:11]+"-"*9+binary[20:22]
    return {       
       "10111000001"+"-"*9+"10" : executor_loadStore.execSTR_reg_offset_32,
       "10111000011"+"-"*9+"10" : executor_loadStore.execLDR_reg_offset_32,
       "10111000101"+"-"*9+"10" : executor_loadStore.execLDRSW_reg_offset,
       "11111000001"+"-"*9+"10" : executor_loadStore.execSTR_reg_offset_64,
       "11111000011"+"-"*9+"10" : executor_loadStore.execLDR_reg_offset_64,
    }[key](binary)
       