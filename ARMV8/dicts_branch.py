'''
@author: harinder
'''

def INSTRUCTION_TYPE(binary,i):
    try:
        return {
            0 : UNCONDITIONAL_BRANCH_IMMEDIATE,
            1 : UNCONDITIONAL_BRANCH_REGISTER,
            2 : CONDITIONAL_BRANCH_IMMEDIATE,
            3 : COMPARE_AND_BRANCH_IMMEDIATE,
        }[i](binary)
    except KeyError:
        i=i
    
def UNCONDITIONAL_BRANCH_IMMEDIATE(binary):
    key = binary[0:6]
    return {
       "000101" : executor_branch.execB,
       "100101" : executor_branch.execBL,
    }[key](binary)
    
def UNCONDITIONAL_BRANCH_REGISTER(binary):
    key = binary[0:21]+"-"*5+binary[25:30]
    return {
       "110101100001111000000-----00000" : executor_branch.execBR,
       "110101100011111000000-----00000" : executor_branch.execBLR,
       "110101100101111000000-----00000" : executor_branch.execRET,
    }[key](binary)
    
def CONDITIONAL_BRANCH_IMMEDIATE(binary):
    key = binary[0:8]+"-"*19+binary[27]
    return {
       "01010100"+"-"*19+"0" : executor_branch.execBCOND,
    }[key](binary)
    
def COMPARE_AND_BRANCH_IMMEDIATE(binary):
    key = binary[0:8]
    return {
       "00110100" : executor_branch.execCBZ_32,
       "00110101" : executor_branch.execCBNZ_32,
       "10110100" : executor_branch.execCBZ_64,
       "10110101" : executor_branch.execCBNZ_64,
    }[key](binary)
