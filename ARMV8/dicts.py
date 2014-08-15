'''
@author: harinder
'''
import executor_addSub
import executor_logical
import executor_move
import executor_shift
import executor_pcRel

def INSTRUCTION_TYPE(binary,i):
    try:
        return {
            0 : ADD_SUB_IMMEDIATE,
            1 : MOVE_IMMEDIATE,
            2 : ADD_SUB_EXT_REG,
            3 : ADD_SUB_SHIFT_REG,
            4 : LOGICAL_SHIFT_REG,
            5 : SHIFT_REGISTER,
            6 : LOGICAL_IMMEDIATE,
            7 : PC_RELATIVE,
        }[i](binary)
    except KeyError:
        i=i

def ADD_SUB_IMMEDIATE(binary):
    key = binary[0:8] 
    return {
       "00010001" : executor_addSub.execAdd_i32,
       "00110001" : executor_addSub.execAdds_i32,
       "01010001" : executor_addSub.execSub_i32,
       "01110001" : executor_addSub.execSubs_i32,
       "10010001" : executor_addSub.execAdd_i64,
       "10110001" : executor_addSub.execAdds_i64,
       "11010001" : executor_addSub.execSub_i64,
       "11110001" : executor_addSub.execSubs_i64,
    }[key](binary)
      
def ADD_SUB_SHIFT_REG(binary):
    key = binary[0:8]
    return {
       "00001011" : executor_addSub.execAdd_sr32,
       "00101011" : executor_addSub.execAdds_sr32,
       "01001011" : executor_addSub.execSub_sr32,
       "01101011" : executor_addSub.execSubs_sr32,
       "10001011" : executor_addSub.execAdd_sr64,
       "10101011" : executor_addSub.execAdds_sr64,
       "11001011" : executor_addSub.execSub_sr64,
       "11101011" : executor_addSub.execSubs_sr64,
    }[key](binary)
    
def ADD_SUB_EXT_REG(binary):
    key = binary[0:11]
    return {
       "00001011001" : executor_addSub.execAdd_er32,
       "00101011001" : executor_addSub.execAdds_er32,
       "01001011001" : executor_addSub.execSub_er32,
       "01101011001" : executor_addSub.execSubs_er32,
       "10001011001" : executor_addSub.execAdd_er64,
       "10101011001" : executor_addSub.execAdds_er64,
       "11001011001" : executor_addSub.execSub_er64,
       "11101011001" : executor_addSub.execSubs_er64,
    }[key](binary) 
    
    
def LOGICAL_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100100" : executor_logical.execAnd_i32,
       "100100100" : executor_logical.execAnd_i64,
    }[key](binary)
    
def LOGICAL_SHIFT_REG(binary):
    key = binary[0:8]+"--"+binary[10]
    return {
       "00001010--0" : executor_logical.execAnd_sr32,
       "10001010--0" : executor_logical.execAnd_sr64,
    }[key](binary)


def MOVE_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100101" : executor_move.execMov_iwi32,
       "100100101" : executor_move.execMov_iwi64,
       "010100101" : executor_move.execMov_wi32,
       "110100101" : executor_move.execMov_wi64,
       "001100100" : executor_move.execMov_bmi32,
       "101100100" : executor_move.execMov_bmi64,
    }[key](binary)
    
        
def SHIFT_REGISTER(binary):
    key = binary[0:11]+"-"*5+binary[16:22]
    return {
       "00011010110-----001010" : executor_shift.execAsr_r32,
       "10011010110-----001010" : executor_shift.execAsr_r64,
       "00011010110-----001000" : executor_shift.execLsl_r32,
       "10011010110-----001000" : executor_shift.execLsl_r64,
       "00011010110-----001001" : executor_shift.execLsr_r32,
       "10011010110-----001001" : executor_shift.execLsr_r64,
    }[key](binary)
    
def PC_RELATIVE(binary):
    key = binary[0]+"--"+binary[3:8]
    return {       
       "0--10000" : executor_pcRel.execADR,
       "1--10000" : executor_pcRel.execADRP,
    }[key](binary)
    
