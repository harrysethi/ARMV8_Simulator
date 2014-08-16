'''
@author: harinder
'''
import executor_addSub
import executor_logical
import executor_move
import executor_shift
import executor_misc

def INSTRUCTION_TYPE(binary, i):
    try:
        return {
            0 : ADD_SUB_IMMEDIATE,
            1 : MOVE_IMMEDIATE,
            2 : MOVE_REGISTER,
            3 : ADD_SUB_EXT_REG,
            4 : ADD_SUB_SHIFT_REG,
            5 : LOGICAL_SHIFT_REG,
            6 : SHIFT_REGISTER,
            7 : SHIFT_IMMEDIATE,
            8 : LOGICAL_IMMEDIATE,
            9 : PC_RELATIVE,
            10 : NOP,
        }[i](binary)
    except KeyError:
        i = i

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
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001011--0" : executor_addSub.execAdd_sr32,
       "00101011--0" : executor_addSub.execAdds_sr32,
       "01001011--0" : executor_addSub.execSub_sr32,
       "01101011--0" : executor_addSub.execSubs_sr32,
       "10001011--0" : executor_addSub.execAdd_sr64,
       "10101011--0" : executor_addSub.execAdds_sr64,
       "11001011--0" : executor_addSub.execSub_sr64,
       "11101011--0" : executor_addSub.execSubs_sr64,
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
    key = binary[0:8] + "--" + binary[10]
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
    
def MOVE_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:27]
    return {
       "00101010000-----00000011111" : executor_move.execMov_r32,
       "10101010000-----00000011111" : executor_move.execMov_r64,
    }[key](binary)


def SHIFT_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
       "00011010110-----001010" : executor_shift.execAsr_r32,
       "10011010110-----001010" : executor_shift.execAsr_r64,
       "00011010110-----001000" : executor_shift.execLsl_r32,
       "10011010110-----001000" : executor_shift.execLsl_r64,
       "00011010110-----001001" : executor_shift.execLsr_r32,
       "10011010110-----001001" : executor_shift.execLsr_r64,
    }[key](binary)
    
def SHIFT_IMMEDIATE(binary):
    key = binary[0:10]
    return {
       "0001001100" : executor_shift.execAsr_i32,
       "1001001101" : executor_shift.execAsr_i64,
       "0101001100" : executor_shift.execLslLsr_i32,
       "1101001101" : executor_shift.execLslLsr_i64,
    }[key](binary)

def PC_RELATIVE(binary):
    key = binary[0] + "--" + binary[3:8]
    return {       
       "0--10000" : executor_misc.execADR,
       "1--10000" : executor_misc.execADRP,
    }[key](binary)
    
def NOP(binary):
    key = binary[0:20] + "-"*7 + binary[27:32]
    return {
       "11010101000000110010" + "-"*7 + "11111" : executor_misc.execNOP,
    }[key](binary)
