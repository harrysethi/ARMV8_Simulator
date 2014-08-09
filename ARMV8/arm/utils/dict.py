'''
Created on Aug 8, 2014

@author: harinder
'''
from arm.execute import executor_addSub, executor_move
from arm.execute import executor_logical

def ADD_SUB_IMMEDIATE(binary):
    key = binary[0:9] 
    return {
       "00010001" : executor_addSub.execAdd_i32,
       "00110001" : executor_addSub.execAdds_i32,
       "01010001" : executor_addSub.execSub_i32,
       "01110001" : executor_addSub.execSubs_i32,
       "00010001" : executor_addSub.execAdd_i64,
       "00110001" : executor_addSub.execAdds_i64,
       "01010001" : executor_addSub.execSub_i64,
       "01110001" : executor_addSub.execSubs_i64,
    }[key](binary)
      
def ADD_SUB_SHIFT_REG(binary):
    key = binary[0:9]
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
    key = binary[0:12]
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
    key = binary[0:10]
    return {
       "000100100" : executor_logical.execAnd_i32,
       "100100100" : executor_logical.execAnd_i64,
    }[key](binary)
    
def LOGICAL_SHIFT_REG(binary):
    key = binary[0:9]+'--'+binary[11]
    return {
       "00001010--0" : executor_logical.execAnd_sr32,
       "10001010--0" : executor_logical.execAnd_sr64,
    }[key](binary)


def MOVE_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100101" : executor_move.execMov_i,
       "100100101" : executor_move.execMov_i,
       "010100101" : executor_move.execMov_i,
       "110100101" : executor_move.execMov_i,
       "001100100" : executor_move.execMov_bmi32,
       "101100100" : executor_move.execMov_bmi64,
    }[key](binary)
    
