'''
@author: harinder
'''
import executor_pcRel

def INSTRUCTION_TYPE(binary,i):
    try:
        return {
            0 : LOAD_REGISTER_LITERAL,
            1 : LOAD_STORE_REGISTER_PAIR_POSTINDEXED,
            2 : LOAD_STORE_REGISTER_PAIR_PREINDEXED,
            3 : LOAD_STORE_REGISTER_PAIR_OFFSET,
            4 : LOAD_STORE_REGISTER_POSTINDEXED_IMMEDIATE,
            5 : LOAD_STORE_REGISTER_PREINDEXED_IMMEDIATE,
            6 : LOAD_STORE_REGISTER_OFFSET,
            7 : LOAD_STORE_REGISTER_UNSIGNED_IMMEDIATE,
        }[i](binary)
    except KeyError:
        i=i

    
def LOAD_REGISTER_LITERAL(binary):
    key = binary[0]+"--"+binary[3:8]
    return {       
       "" : executor_pcRel.execADR,
       "" : executor_pcRel.execADRP,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PAIR_POSTINDEXED(binary):
    key = binary[0]+"--"+binary[3:8]
    return {       
       "" : executor_pcRel.execADR,
       "" : executor_pcRel.execADRP,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PAIR_PREINDEXED(binary):
    key = binary[0]+"--"+binary[3:8]
    return {       
       "" : executor_pcRel.execADR,
       "" : executor_pcRel.execADRP,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PAIR_OFFSET(binary):
    key = binary[0]+"--"+binary[3:8]
    return {       
       "" : executor_pcRel.execADR,
       "" : executor_pcRel.execADRP,
    }[key](binary)
    
def LOAD_STORE_REGISTER_POSTINDEXED_IMMEDIATE(binary):
    key = binary[0]+"--"+binary[3:8]
    return {       
       "" : executor_pcRel.execADR,
       "" : executor_pcRel.execADRP,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PREINDEXED_IMMEDIATE(binary):
    key = binary[0]+"--"+binary[3:8]
    return {       
       "" : executor_pcRel.execADR,
       "" : executor_pcRel.execADRP,
    }[key](binary)
    
def LOAD_STORE_REGISTER_OFFSET(binary):
    key = binary[0]+"--"+binary[3:8]
    return {       
       "" : executor_pcRel.execADR,
       "" : executor_pcRel.execADRP,
    }[key](binary)
    
def LOAD_STORE_REGISTER_UNSIGNED_IMMEDIATE(binary):
    key = binary[0]+"--"+binary[3:8]
    return {       
       "" : executor_pcRel.execADR,
       "" : executor_pcRel.execADRP,
    }[key](binary)
